
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=1)
 
    def forward(self, x):
        v  = self.conv_transpose(x) + 3
        v  = torch.clamp(v, min=0)
        v /= 6
        return v


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(1, 8, 64, 64)
