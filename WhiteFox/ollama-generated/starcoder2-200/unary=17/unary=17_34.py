
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x):
        v = self.convT(x)
        return v


# Initializing the model
m2  = Model2()
 
# Inputs to the model
input__tensor  = torch.randn(4503798776135, 3, 256, 256) # A randomly generated input tensor of shape [N, C, H, W] for a conv_transpose layer with kernel size 1

