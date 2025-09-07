
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(8, 3, kernel_size=1)
 
    def forward(self, x):
        t1 = self.deconv(x)
        t2 = torch.sigmoid(t1)
        return t2

# Initializing the model
m = Model()
 
# Inputs to the model
x = torch.randn(1, 8, 64, 64)
