
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
 
        v3 = torch.mm(input1, input2) + torch.mm(input3, input4)
        return v3


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
