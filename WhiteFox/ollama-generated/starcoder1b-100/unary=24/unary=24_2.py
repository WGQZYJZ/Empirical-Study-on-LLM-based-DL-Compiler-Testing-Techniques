
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = F.relu(self.conv(x1))
        v2 = x1 * -0.5 + F.leaky_relu(-v1, negative_slope=0.00001) # Use the where function to multiply the output of the convolution and then subtract a small value from it
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
