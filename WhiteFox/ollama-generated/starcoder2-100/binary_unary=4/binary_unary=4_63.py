
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear  = torch.nn.Linear(4096, 512)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1 + other


# Initializing the model and passing an argument to it.
m  = Model(other=torch.randn((1)))

# Inputs to the model
x1  = torch.randn(1, 4096)
__output__  = m(x1)

