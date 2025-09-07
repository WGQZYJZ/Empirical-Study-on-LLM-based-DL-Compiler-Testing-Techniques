
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
        self.other = None
 
    def forward(self, x1):
        v1 = self.linear(x1) + self.other
        return v1


# Initializing the model
m = Model()

 # Input tensor to the model
x1 = torch.randn(32, 32, dtype=torch.float)
 
# Other tensor for linear transformation with input dimensions [64 x 64]
o = torch.randn(64, 64, dtype=torch.float)
m.other = o


