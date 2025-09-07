
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, input1, x2, input2):
        v1 = self.conv(x1)
        v2 = v1 + input1
        return v2


# Inputs to the model
input1 = torch.randn(3, 64, 64)
input2 = torch.randn(1, 8, 64, 64)
