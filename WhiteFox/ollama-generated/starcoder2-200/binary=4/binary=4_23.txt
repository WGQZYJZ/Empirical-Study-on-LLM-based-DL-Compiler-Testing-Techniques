
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(819200, 73400)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + torch.randn(v1.shape[0], v1.shape[-1]) # Use a random tensor as the "other" keyword argument
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 8192)
__output__  = m(x1)

