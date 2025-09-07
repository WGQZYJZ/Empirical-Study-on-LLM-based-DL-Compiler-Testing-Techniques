
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @classmethod
    def from_config(cls, config: Config, parent: 'Optional[Model] = None', *args, **kwargs) -> 'Model':
        