
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv = torch.nn.ConvTranspose1d(8, 3, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = (v1 > 0).type_as(v1)
        v3  = v1 * negative_slope
        v4  = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(80000, 64, 512) # Batch size of 8, input dimension is 512

__output__  = m(x1).shape
