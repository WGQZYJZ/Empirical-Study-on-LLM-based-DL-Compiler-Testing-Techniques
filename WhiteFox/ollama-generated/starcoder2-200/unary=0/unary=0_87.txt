
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 ** 3 # Square the output of the convolution
        v4 = v3 * v1  # Cube the output of the convolution
        v5 = torch.tanh((v4 + 0.7978845608028654) * v2) 
        return ((torch.abs(v2 + (0.044715 * v3))) * (((-0.5 * x1) + (-v5))))

# Initializing the model
m = Model()

