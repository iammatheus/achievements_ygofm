from winotify import Notification, audio
from achievements.classes.achievement_base import AchievementBase
from const.rare_cards import RARE_CARDS
from const.rare_cards_images import RARE_CARDS_IMAGES
from pathlib import Path

def show_starchips_achievement(achievement: AchievementBase, _):
    toast = Notification(
        app_id='🏆 Conquista desbloqueada!',
        title=achievement.title,
        msg=achievement.msg,
        icon=Path("assets/starchip.png").resolve(),
    )
    toast.set_audio(audio.SMS, loop=False)
    toast.show()

def show_secret_rare_card_progress_achievement(achievement: AchievementBase, card_id):
    # Se card_id for None => Cai no return.
    # Se card_id for int => Pula return e imprime Notification.
    # Consultar >>classes/achievement_manager<< para entender fluxo.
    # Resumo: 
    #   Se for None => desbloqueou a conquista: unlocked = true.
    #   Se não e houver card_id => Somente progress é preenchido com o número da carta e unlocked permanece como false.

    if card_id is None:
        return

    card_name = RARE_CARDS[card_id]
    card_icon = RARE_CARDS_IMAGES[card_id]
   
    toast = Notification(
        app_id = achievement.title,
        title=f"{card_name}",
        msg=f"{len(achievement.progress)}/{achievement.total}",
        icon=card_icon,
    )
    toast.set_audio(audio.SMS, loop=False)
    toast.show()