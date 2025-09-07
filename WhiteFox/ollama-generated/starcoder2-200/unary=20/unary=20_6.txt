
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(32, 16, 4)
 
    def forward(self, x):
        v0 = self.deconv(x)
        v1 = torch.sigmoid(v0)
        return v1

# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(32, 64, 8, 9) # 32 batch size with height and width of 8 by 9
