
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor = None) -> None:
        super().__init__()
        self.linear  = torch.nn.Linear(3072, 1568)
        self.__other__ = other

    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + self.__other__ 
        v3  = F.relu(v2)  
        return v3


# Initializing the model with keyword argument `other` and passing the torch tensor as a keyword argument value
m  = Model(torch.randn(1, 3072))

 # Inputs to the model 
__output__  = m(x1).flatten()