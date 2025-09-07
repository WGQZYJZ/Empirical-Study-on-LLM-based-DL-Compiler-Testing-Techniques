
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v2 ** 2
        v4  = v3 * v1
        v5  = torch.log(v4 + 4) / (-4.785946588333784e+14) # Add a constant to avoid logarithm underflow
        v6  = v2 + v5 
        v7  = (v6 * tanh(0.7978845608028654)) + 1 
        v8  = v3 * v7 
        return v8


# Initializing the model