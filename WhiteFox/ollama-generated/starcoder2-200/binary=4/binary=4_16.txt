
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048,1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + torch.rand((3,5)) # another random tensor
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(64, 2048)
__output__  = m(x1)

