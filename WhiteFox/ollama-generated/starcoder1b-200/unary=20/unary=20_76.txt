
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, kernel_size=1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return torch.sigmoid(v1)


# Initializing the model
m = Model()

# Inputs to the model
input_tensor  = torch.randn(32, 3, 64, 64) # This is an input tensor
__output__  = m(input_tensor)           # This is the output of the model
