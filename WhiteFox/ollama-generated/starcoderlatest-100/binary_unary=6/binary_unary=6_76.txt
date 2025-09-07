
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(1024, 1024)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        v3 = torch.relu(v2)
        return v3


# Inputs to the model
x1 = torch.randn(1, 1024, 64, 64)
other = torch.randn(1, 1024, 64, 64)
