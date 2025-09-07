
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @classmethod
    def replace_dropouts(cls, model: nn.Module):
        model.features = nn.Dropout()
        model.classifier = nn.Linear(...)
