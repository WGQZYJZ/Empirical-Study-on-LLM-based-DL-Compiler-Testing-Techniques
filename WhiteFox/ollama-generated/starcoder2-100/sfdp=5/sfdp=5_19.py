
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v0 = torch.zeros_like(x1)
        v7 = v0  # Replace with a new tensor
        v1  = self.conv(v7) + (x1 + 3.) * .5 + .25
        v8 = v0
        v9 = v1 @ v8  # Replace with a new tensor
        v10 = torch.nn.ConvTranspose2d(in_channels=8, out_channels=4, kernel_size=(1, 1), stride=(1, 1), padding=(-1, -1))
        return x1


# Initializing the model
m  = Model()
# Inputs to the model
x1  = torch.randn(20,3,64,64)
__output__  = m(x1)

