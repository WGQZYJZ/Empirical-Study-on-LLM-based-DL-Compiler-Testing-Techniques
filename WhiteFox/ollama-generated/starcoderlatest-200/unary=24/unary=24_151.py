
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = (v1 > 0).float()
        negative_slope = -negative_slope # Make the output of multiplying by the negative slope a parameter of this layer
        v4 = torch.where(mask, v1 * negative_slope, v1) # Apply the where function to select elements from the output of the convolution or the result of the multiplication based on the mask
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
