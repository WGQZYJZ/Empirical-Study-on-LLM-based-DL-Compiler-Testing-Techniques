
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        
        negative_slope  = 0.5
        v1 = conv_transpose(x1)
        v2 = v1 > 0 
        v4 = v1 * -negative_slope
        v5 = torch.where(v2, t1, v4)

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)
