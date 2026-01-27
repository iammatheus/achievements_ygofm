from winotify import Notification, audio
from const.rare_cards import RARE_CARDS
from const.rare_cards_images import RARE_CARDS_IMAGES

def show_achievement(achievement, card_name=None):
    msg = achievement.title
    if card_name:
        msg = f"Você obteve: {card_name}"

    Notification(
        app_id="Yu-Gi-Oh! FM MOD 11",
        title="🏆 Conquista desbloqueada!",
        msg=msg,
    ).show()

def show_rare_card_progress(achievement, card_id):
    card_name = RARE_CARDS[card_id]
    card_icon = RARE_CARDS_IMAGES[card_id]
   
    toast = Notification(
        app_id="Yu-Gi-Oh! FM MOD 11",
        title="🏆 Carta Rara Obtida!",
        msg=(
            f"{card_name}\n"
            f"{len(achievement.progress)}/{achievement.total + 1}" 
        ),
        icon=card_icon,
    )
    toast.set_audio(audio.SMS, loop=False)
    toast.show()