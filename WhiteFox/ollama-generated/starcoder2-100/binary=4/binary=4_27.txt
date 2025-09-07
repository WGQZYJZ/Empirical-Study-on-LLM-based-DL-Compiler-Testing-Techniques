
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32,10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        return v1 + self.__output__


# Initializing the model and setting the additional tensor "other" as a random tensor:
m  = Model()
other  = torch.randn(32,) # This is an example of the additional tensor (other) used in the pattern
__output__  = m(x1, other=other)

