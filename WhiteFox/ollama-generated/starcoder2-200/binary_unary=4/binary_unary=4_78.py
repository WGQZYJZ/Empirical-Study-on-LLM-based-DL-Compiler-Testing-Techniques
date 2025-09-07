
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = self.__output__
        other  = torch.randn((30784,)) # Generating a randomly sized tensor
        v1  = torch.nn.Linear(v2.size(-1), 10)(x1)
        v3  = torch.nn.ReLU()(v1 + other)
        return v3


# Initializing the model