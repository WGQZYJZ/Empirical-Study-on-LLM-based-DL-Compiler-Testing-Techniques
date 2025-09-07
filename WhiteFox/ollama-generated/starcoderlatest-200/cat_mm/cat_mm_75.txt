
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        t1 = torch.mm(v1, x2) # Matrix multiplication of the output of the pointwise convolution with two input tensors
        v2 = torch.cat([t1] * len(input2), dim=1) # Concatenation along a dimension equal to 1
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
