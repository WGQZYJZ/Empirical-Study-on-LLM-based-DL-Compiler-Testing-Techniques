
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1 * v1 * v1 # V1 is being cubed
        v4  = v3 * 0.044715 
        v5  = v1 + v4
        v6  = v5 * 0.7978845608028654 
        v7  = torch.tanh(v6)
        v8  = v7 + 1 # V7 is being added to 1. The value of v7 is always going to be between -1 and 1 after applying hyperbolic tangent function. As a result, the range of v7 will stay constant from 0 to 2
        v9  = v2 * v8 
        return v9


# Initializing the model