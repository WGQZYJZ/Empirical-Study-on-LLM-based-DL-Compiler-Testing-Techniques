
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3 # Add 3 to the output of the convolution
        v3  = F.relu6(v2) # Clamp the output of the addition operation to a minimum of 0 and a maximum of 6
        v4  = v3 * 8 
        v5  = v4 / 6
        return v5

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(2, 3, 100, 100)

__output__  = m(x1)

