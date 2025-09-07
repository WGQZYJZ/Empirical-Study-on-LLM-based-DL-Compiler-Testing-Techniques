
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(64 * 56 * 10, 512)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.linear(v1.view(-1))
        v3 = torch.sigmoid(v2)
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
