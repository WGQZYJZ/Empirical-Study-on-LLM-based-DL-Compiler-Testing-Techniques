
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask  = v1 > 0 # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        negative_slope  = torch.tensor(negative_slope).view(1, -1, 1, 1)
        v2 = v1 * negative_slope
        v3 = v2 + v1
        return v3


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
