
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(3, 8, kernel_size=3)
 
    def forward(self, x1):
        v0 = self.conv1(x1)
        v1 = torch.tanh(v0)
        return v1


# Initializing the model
m  = Model()
 
 # Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
