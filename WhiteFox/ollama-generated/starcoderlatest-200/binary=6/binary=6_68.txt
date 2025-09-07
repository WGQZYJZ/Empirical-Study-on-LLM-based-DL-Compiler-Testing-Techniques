
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - self.other # Subtract 'other' from the output of the linear transformation
        return v6


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
