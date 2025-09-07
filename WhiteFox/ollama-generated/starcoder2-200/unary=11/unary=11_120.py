
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.tran = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1  = self.conv(x) 
        v2  = self.tran(v1) + 3
        v3  = torch.clamp_min(v2, 0) # Add 6 to the output of the transposed convolution
        v4  = torch.clamp_max(v3, 6) # Clamp the output of the addition operation at a minimum of 0
        v5  = v4 / 6 # Divide the output of the previous operation by 6
        return v5


# Initializing the model
m  = Model()

# Inputs to the model. The shape should match the input size of the previous model.
x1  = torch.randn(1, 3, 28, 28)

__output__  = m(x1)

