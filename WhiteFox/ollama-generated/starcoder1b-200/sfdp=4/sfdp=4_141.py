
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        w1 = torch.softmax(v1 @ self.key.transpose(-2, -1), dim=-1) @ v1
        return w1


# Inputs to the model
query = torch.randn(2, 3, 64, 64)
value = torch.randn(2, 8, 64, 64)
