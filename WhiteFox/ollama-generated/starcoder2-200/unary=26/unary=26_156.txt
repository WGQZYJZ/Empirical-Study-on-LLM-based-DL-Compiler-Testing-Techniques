
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.15):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(32, 48, kernel_size=(10, 10), stride=1)
        self.negative_slope = negative_slope
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4

# Initializing the model
m = Model()

 # Inputs to the model
 x = torch.randn(16, 32, 80, 80)
 
# Output of the model on inputs above
m(x)

