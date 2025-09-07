
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*180, 5)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = F.relu(v1)
        return v2


# Initializing the model
m = Model()
# Inputs to the model
x = torch.randn(320, 32*180)
__output__  = m(x).sum()

