
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 * 0.5
        v3  = v1 * v1 * v1 # V4 
        v4  = v3 * 0.044715 # V5
        v6  = v4 + v2 # V6
        v7  = torch.tanh(v6) # V7
        v8  = v7 + 1 # V8
        v9  = v8 * 0.7978845608028654 # V9 
        return v9

# Initializing the model