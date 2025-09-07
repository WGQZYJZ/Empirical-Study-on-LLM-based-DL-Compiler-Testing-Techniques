
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v0 = self.deconv(x1)
        v1 = torch.relu(v0)
        return v1

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 8, 64, 64)


