
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other # Add another tensor to the output of the convolution
        return v2


# Initializing the model with constant
m1 = Model(1000) 
# Inputs to the model
x1_constant = torch.randn(1, 3, 64, 64)
