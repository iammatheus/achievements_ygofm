from winotify import Notification, audio
from achievements.classes.achievement_base import AchievementBase
from pathlib import Path
from const.app_id import APP_ID

def show_starchips_achievement(achievement: AchievementBase, _):
    toast = Notification(
        APP_ID,
        achievement.title,
        achievement.msg,
        icon=Path("assets/original/starchip.png").resolve(),
    )
    toast.set_audio(audio.SMS, loop=False)
    toast.show()