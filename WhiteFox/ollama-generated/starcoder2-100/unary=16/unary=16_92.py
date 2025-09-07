
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear1 = torch.nn.Linear(32, 64)
        self.relu1 = torch.nn.ReLU()
 
    def forward(self, x):
        v1 = self.linear1(x)
        v2 = self.relu1(v1)
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x  = torch.randn(64, 32)
__output__  = m(x)