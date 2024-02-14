from dataclasses import dataclass, field

@dataclass
class Message:
    chat_id : str = None
    message_id : str = None
    username : str = None
    last_name : str = None
    first_name : str = None
    text : str = None
    photo : str = None
    voice : str = None
    video_note : str = None
    video : str = None
    document : str = None
    callback : str = None
    error : bool = field(init=False)

    def __post_init__(self):
        if not self.chat_id  or not self.message_id:
            self.error = True
        else:
            self.error = False