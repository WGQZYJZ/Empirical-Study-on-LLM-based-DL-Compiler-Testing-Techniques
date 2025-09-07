
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, kernel_size=2)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
input_tensor  = torch.randn(1, 8, 64, 64)
__output__    = m(input_tensor)

