
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(24, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.tanh(v1) # Replace with a specific tanh function from PyTorch if necessary 
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(64, 24)
__output__  = m(x1)

