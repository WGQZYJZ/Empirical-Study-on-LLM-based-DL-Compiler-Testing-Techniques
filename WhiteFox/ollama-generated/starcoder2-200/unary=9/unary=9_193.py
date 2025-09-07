
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0) # Min value to clamp to is set as zero
        v4  = torch.clamp_max(v3, 6) # Max value to clamp to is set as six
        v5  = v4 / 6 
        return v5

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 227, 227)
__output__  = m(x1)

