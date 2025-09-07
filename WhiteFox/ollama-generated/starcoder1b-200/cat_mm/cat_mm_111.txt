
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1)
 
    def forward(self, x1, x2):
        v1 = self.conv1(x1) + self.conv2(x2)
        return v1


# Inputs to the model
input1  = torch.randn(3, 1, 64, 64)
input2  = torch.randn(8, 1, 64, 64)
