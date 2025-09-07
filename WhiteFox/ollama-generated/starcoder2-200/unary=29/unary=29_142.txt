
class Model(torch.nn.Module):
    def __init__(self, minv=1234567890123.4567890123e-9, maxv=0.987654321):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, min_value=0.75e-9) 
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3, 8, 64, 64)
