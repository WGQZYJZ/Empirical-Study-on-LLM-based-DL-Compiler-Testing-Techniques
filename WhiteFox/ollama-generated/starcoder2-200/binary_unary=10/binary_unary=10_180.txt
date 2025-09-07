
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 3)
        self.other = torch.randn(64)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + self.other
        v3  = F.relu(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(10, 128) # Input tensor of size 10 x 128
__output__  = m(x1)