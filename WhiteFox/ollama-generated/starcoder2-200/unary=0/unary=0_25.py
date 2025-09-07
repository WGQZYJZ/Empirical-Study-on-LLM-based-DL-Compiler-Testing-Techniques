
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1   = self.conv(x1)
        v2   = v1 * 0.5
        v3   = v1 ** 3
        v4   = v3 * 0.044715 
        v6   = v1 + v4 
        v8   = torch.tanh(v6) * 0.7978845608028654  
        v10  = v8 + 1
        v11  = v2 * v10
        return v11


# Initializing the model and inputs to the model, respectively
m  = Model()
x1 = torch.randn(1, 3, 64, 64)
 
