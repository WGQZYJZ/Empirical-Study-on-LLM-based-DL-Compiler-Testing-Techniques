
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1
 
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32)
