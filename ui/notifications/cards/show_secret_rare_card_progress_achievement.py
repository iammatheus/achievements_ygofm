from winotify import Notification, audio
from achievements.classes.achievement_base import AchievementBase
from pathlib import Path
from memory.repositories.card_repository import CardRepository
from memory.entities.card_entity import CardEntity
from paths import ALL_CARDS_PATH
from utils import progress_bar_util
from const.app_id import APP_ID

def show_secret_rare_card_progress_achievement(achievement: AchievementBase, card_id: int):
    # Se card_id for None => Cai no return.
    # Se card_id for int => Pula return e imprime Notification.
    # Consultar >>classes/achievement_manager<< para entender fluxo.
    # Resumo: 
    #   Se for None => desbloqueou a conquista: unlocked = true.
    #   Se não e houver card_id => Somente progress é preenchido com o número da carta e unlocked permanece como false.
    if card_id is None:
        return
    
    cardRepository = CardRepository(ALL_CARDS_PATH)
    card: CardEntity | None = cardRepository.get_by_id(card_id)

    if card is None:
        return
    
    iconMessage: str = "🏅"
    progress_bar: str = progress_bar_util(len(achievement.progress), achievement.total)
    
    if len(achievement.progress) >= achievement.total:
        achievement.title = "VOCÊ OBTEVE TODAS AS 82 RARAS!\n"
        iconMessage = "🏆"
    
    toast = Notification(
        APP_ID,
        achievement.title,
        msg=(
            f"{card.name}\n"
            f"{iconMessage}({len(achievement.progress)}/{achievement.total})\n"
            f"{progress_bar}"
        ),
        icon=Path(card.image).resolve(),
    )
    toast.set_audio(audio.SMS, loop=False)
    toast.show()