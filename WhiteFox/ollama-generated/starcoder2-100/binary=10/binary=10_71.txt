
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = self.__other__  # An additional tensor
        v1 = torch.nn.Linear(32768, 4096)(x1)
        v2 = v1 + v0
        return v2
 
__model__ = Model()


# Initializing the model