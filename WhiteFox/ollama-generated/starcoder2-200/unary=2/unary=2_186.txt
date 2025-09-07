
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 ** 3 # Cube the output of the transposed convolution
        v4 = torch.mul(v3, 0.044715) # Multiply the cubed output by 0.044715
        v5 = v1 + v4 
        v6 = torch.mul(v5, 0.7978845608028654) # Multiply the output of the addition by 0.7978845608028654
        v7 = torch.tanh(v6) 
        v8 = torch.mul(v1, v7) + 1
        return v8

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(30, 95, 247, 197)
__output__  = m(x1)