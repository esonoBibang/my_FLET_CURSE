"""
Detector de Apertura de Sesión de Nueva York (Forex)
------------------------------------------------------
App hecha con Flet que muestra:
- Hora actual en Nueva York
- Cuenta regresiva hasta la apertura de la sesión
- Alerta visual/sonora cuando la sesión abre
- Estado actual: ABIERTA / CERRADA

Requisitos:
    pip install flet

Ejecutar:
    python ny_session_detector.py
"""

import flet as ft
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import threading
import time

# ----------------------------
# Configuración de la sesión
# ----------------------------
NY_TZ = ZoneInfo("America/New_York")

# Horario de la sesión de Nueva York (hora local NY)
SESSION_OPEN_HOUR = 8   # 8:00 AM ET (apertura considerada por muchos traders)
SESSION_CLOSE_HOUR = 17  # 5:00 PM ET (cierre aproximado)


def get_ny_now() -> datetime:
    return datetime.now(NY_TZ)


def get_next_open(now: datetime) -> datetime:
    """Calcula el próximo datetime de apertura de sesión (hoy o mañana)."""
    open_today = now.replace(hour=SESSION_OPEN_HOUR, minute=0, second=0, microsecond=0)
    if now >= open_today:
        # Ya pasó la apertura de hoy -> calcular la de mañana
        return open_today + timedelta(days=1)
    return open_today


def is_session_open(now: datetime) -> bool:
    """True si la hora actual está dentro del rango de sesión."""
    open_time = now.replace(hour=SESSION_OPEN_HOUR, minute=0, second=0, microsecond=0)
    close_time = now.replace(hour=SESSION_CLOSE_HOUR, minute=0, second=0, microsecond=0)
    # Nota: no considera fines de semana (forex cierra sáb-dom)
    is_weekday = now.weekday() < 5  # 0=Lunes ... 4=Viernes
    return is_weekday and open_time <= now < close_time


def format_timedelta(td: timedelta) -> str:
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def main(page: ft.Page):
    page.title = "Detector de Sesión de Nueva York"
    page.window.width = 480
    page.window.height = 520
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30

    # --- Elementos de UI ---
    titulo = ft.Text("Sesión de Nueva York (Forex)", size=22, weight=ft.FontWeight.BOLD)

    hora_ny_text = ft.Text(size=40, weight=ft.FontWeight.BOLD, font_family="Consolas")
    fecha_ny_text = ft.Text(size=14, color=ft.Colors.GREY_400)

    estado_badge = ft.Container(
        content=ft.Text("CARGANDO...", size=16, weight=ft.FontWeight.BOLD),
        padding=ft.Padding.symmetric(horizontal=20, vertical=8),
        border_radius=20,
        bgcolor=ft.Colors.GREY_700,
    )

    countdown_label = ft.Text("Tiempo hasta la apertura:", size=14, color=ft.Colors.GREY_400)
    countdown_text = ft.Text(size=32, weight=ft.FontWeight.BOLD, font_family="Consolas")

    alerta_banner = ft.Container(
        content=ft.Text(
            "🔔 ¡LA SESIÓN DE NUEVA YORK ACABA DE ABRIR!",
            size=16,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE,
            text_align=ft.TextAlign.CENTER,
        ),
        bgcolor=ft.Colors.GREEN_700,
        padding=15,
        border_radius=10,
        visible=False,
        animate_opacity=300,
    )

    info_text = ft.Text(
        f"Apertura configurada: {SESSION_OPEN_HOUR:02d}:00 ET | Cierre: {SESSION_CLOSE_HOUR:02d}:00 ET\n"
        "(No opera fines de semana)",
        size=12,
        color=ft.Colors.GREY_500,
        text_align=ft.TextAlign.CENTER,
    )

    page.add(
        ft.Column(
            [
                titulo,
                ft.Divider(),
                hora_ny_text,
                fecha_ny_text,
                ft.Container(height=15),
                estado_badge,
                ft.Container(height=20),
                alerta_banner,
                ft.Container(height=15),
                countdown_label,
                countdown_text,
                ft.Container(height=20),
                info_text,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5,
        )
    )

    # --- Lógica de actualización en segundo plano ---
    stop_event = threading.Event()
    was_open_previously = {"value": False}

    def update_loop():
        while not stop_event.is_set():
            now = get_ny_now()
            session_open = is_session_open(now)

            # Detectar el MOMENTO EXACTO de apertura (transición cerrada -> abierta)
            just_opened = session_open and not was_open_previously["value"]
            was_open_previously["value"] = session_open

            # Actualizar hora y fecha
            hora_ny_text.value = now.strftime("%H:%M:%S")
            fecha_ny_text.value = now.strftime("%A, %d de %B de %Y") + " (Hora de Nueva York)"

            # Actualizar estado
            if session_open:
                estado_badge.content.value = "🟢 SESIÓN ABIERTA"
                estado_badge.bgcolor = ft.Colors.GREEN_700
            else:
                estado_badge.content.value = "🔴 SESIÓN CERRADA"
                estado_badge.bgcolor = ft.Colors.RED_700

            # Cuenta regresiva hasta próxima apertura
            if not session_open:
                next_open = get_next_open(now)
                remaining = next_open - now
                countdown_label.value = "Tiempo hasta la apertura:"
                countdown_text.value = format_timedelta(remaining)
            else:
                close_today = now.replace(hour=SESSION_CLOSE_HOUR, minute=0, second=0, microsecond=0)
                remaining = close_today - now
                countdown_label.value = "Tiempo hasta el cierre:"
                countdown_text.value = format_timedelta(remaining)

            # Mostrar alerta si justo abrió
            if just_opened:
                alerta_banner.visible = True
                page.update()
                # Reproducir sonido del sistema si se desea (opcional, requiere configuración extra)
            elif alerta_banner.visible and not session_open:
                # Ocultar alerta si ya se cerró de nuevo (reinicia el ciclo)
                alerta_banner.visible = False

            try:
                page.update()
            except Exception:
                break  # La ventana fue cerrada

            time.sleep(1)

    thread = threading.Thread(target=update_loop, daemon=True)
    thread.start()

    def on_window_event(e: ft.WindowEvent):
        if e.type == ft.WindowEventType.CLOSE:
            stop_event.set()

    page.window.on_event = on_window_event


if __name__ == "__main__":
    ft.run(main)