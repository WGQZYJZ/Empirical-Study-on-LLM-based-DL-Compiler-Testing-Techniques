
class Model(torch.nn.Module):
    def __init__(self, b, c):
        super().__init__()
        self.conv = torch.nn.Conv2d(b, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v4 = v1 - other # Subtract 'other' from the output of the convolution
        return v4


# Initializing the model
other = torch.randn([b, c, 64, 64])

# Inputs to the model
x1 = torch.randn(1, b, 64, 64)
