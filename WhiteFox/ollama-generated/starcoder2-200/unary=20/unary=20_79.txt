
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3,8,1)
 
    def forward(self, x):
        v0   = self.conv(x)
        return torch.sigmoid(v0)

# Initializing the model
m  = Model()

 # Inputs to the model
__inputs__ = torch.randn(1, 3,64,64)

# Output from the model
