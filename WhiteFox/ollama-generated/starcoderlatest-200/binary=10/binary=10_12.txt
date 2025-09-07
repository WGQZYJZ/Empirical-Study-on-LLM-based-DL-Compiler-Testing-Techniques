
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(128, 64)
 
    def forward(self, x1, other=0):
        v1 = self.conv(x1) + other
        return v1


# Inputs to the model
x1 = torch.randn(1, 128)
