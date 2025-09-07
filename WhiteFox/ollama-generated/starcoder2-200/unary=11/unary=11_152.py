
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv  = torch.nn.ConvTranspose2d(32, 10, 4)

    def forward(self, x):
        v1  = self.deconv(x)
        v2  = v1 + 3
        v3  = F.relu_min(v2, 0)
        v4  = F.relu_max(v3, 6)
        v5  = v4 / 6 
        return v5


# Initializing the model
m  = Model()

 # Inputs to the model 
x1  = torch.randn(1, 10, 32, 8)
__output__  = m(x1)


