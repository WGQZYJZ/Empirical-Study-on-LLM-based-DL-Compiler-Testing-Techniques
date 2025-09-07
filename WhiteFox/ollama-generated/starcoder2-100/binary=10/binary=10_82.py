
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = self._model0(x1)
        v3 = self._model0(other)
        v4  = v2 + v3 
        return v4

# Initializing the model
m  = Model()

