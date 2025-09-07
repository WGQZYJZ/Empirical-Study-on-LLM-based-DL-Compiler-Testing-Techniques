
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, size):
        v1 = [x1] + [x2]
        v4 = torch.cat([v0 for i, v0 in enumerate(v1)], dim=1)
        v5  = v4[:, 0:9223372036854775807]
        v6  = v5[:, 0:size]

        return torch.cat([v4, v6], dim=1)


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 28, 28) # Input tensor shape: [batch size, channel number, height, width]
x2  = torch.randn(1, 3, 56, 56) # Input tensor shape: [batch size, channel number, height, width]
size  = 40 # An integer value
__output__  = m(x1, x2, size)

