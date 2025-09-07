
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v6  = v1 + 10  # Add `10` to the output of the convolution
        return v6


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(2, 3, 480, 75)
__output__  = m(x1)