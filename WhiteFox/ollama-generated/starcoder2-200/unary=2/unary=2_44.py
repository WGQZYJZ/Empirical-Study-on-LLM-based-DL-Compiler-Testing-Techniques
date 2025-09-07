

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x1):
        v1  = self.deconv(x1)
        v2  = v1 * 0.5
        v3  = v1 * v1 
        v4  = v3  * t
        return v9

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
