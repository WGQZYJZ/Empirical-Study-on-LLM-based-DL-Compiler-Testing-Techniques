
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 3, stride=1, padding=1)
 
    def forward(self, x):
        return self.conv2(torch.cat([
            self.conv1(x[:, :32]),
            self.conv1(x[:, 32:64]),
            self.conv1(x[:, 64:])], dim=1))


# Inputs to the model
x = torch.randn(3, 8, 64, 64)
