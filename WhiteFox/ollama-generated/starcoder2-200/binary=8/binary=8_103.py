
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + other
        return v1


# Initializing the model with a new tensor to be added to every convolutional output (in this example it is torch.randn((3))) as keyword argument
m  = Model(torch.randn((3)))

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
