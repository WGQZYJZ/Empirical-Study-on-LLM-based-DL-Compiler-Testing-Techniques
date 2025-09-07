
class Model(torch.nn.Module):
    def __init__(self, other_tensor):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + other_tensor
        return v1


# Initializing the model with another tensor as the input of the pointwise convolution operation
m2 = Model(other_tensor = torch.randn(3, 8))

# Inputs to the model
x2 = torch.randn(1, 3, 64, 64)
