
class TransformerModel(nn.Module):
    def __init__(self, d_model: int = 512) -> None:
        super().__init__()
 
        # embedding layers
        self.position_embedding = nn.Embedding(1024 + 1, d_model)
 
    @property 
    def device(self): 
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")

    @property
    def model_device(self):
        return self._model_device
 
    @model_device.setter
    def model_device(self, value: int) -> None:

        self._model_device = torch.device("cuda:" + str(value))
