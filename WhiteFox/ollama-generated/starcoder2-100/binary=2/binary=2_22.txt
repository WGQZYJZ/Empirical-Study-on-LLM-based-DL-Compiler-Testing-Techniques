
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        return v2

# Initializing the model with a random tensor of shape [batch_size, 3, height, width] for 'other'
other  = torch.randn([4, 8, 64, 64])


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1, other)

