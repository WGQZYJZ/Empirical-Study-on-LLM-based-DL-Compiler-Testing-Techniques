
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3)
        self.conv2 = torch.nn.Conv2d(8, 8, 3)
 
    def forward(self, x1, x2):
        v1 = self.conv1(x1).unsqueeze(0)
        v2 = self.conv2(x2).unsqueeze(0)
        return v2 + v1


# Inputs to the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 5, 5)
