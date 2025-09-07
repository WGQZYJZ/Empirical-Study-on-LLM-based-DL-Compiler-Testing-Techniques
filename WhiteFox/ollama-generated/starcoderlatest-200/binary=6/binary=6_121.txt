
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(64, 3)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        return v2
# Inputs to the model
other = torch.randn(3)
x1 = torch.randn(1, 64, 64)
