
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 4, 2, stride=1, padding=2)
 
    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        return torch.mm(v1, v2)


# Inputs to the model
input1 = torch.randn(3, 8, 64, 64)
input2 = torch.randn(3, 8, 64, 64)
