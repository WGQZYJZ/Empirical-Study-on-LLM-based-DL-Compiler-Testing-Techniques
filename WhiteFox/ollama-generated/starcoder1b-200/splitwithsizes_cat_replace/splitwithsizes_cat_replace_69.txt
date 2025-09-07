
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y2, z3, t4):
        v1 = self.conv(x1)
        return torch.cat([v1, y2], dim=0)

 # Initializing the model
m  = Model()
 
 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
y2 = torch.randn(1, 3, 32, 32)
z3 = torch.randn(1, 8, 32, 32)
t4 = torch.tensor([0.1])

 # Output of the model
