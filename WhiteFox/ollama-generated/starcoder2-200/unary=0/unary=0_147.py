
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1   = self.conv(x1)
        v2   = v1 * 0.5
        v3   = (v1 * v1) ** 3 
        v4   = v3 * 0.044715 
        v6   = v1 + v4  
        v8   = torch.tanh(self.conv(x1))  
        v9   = self.conv(x1)
        v12  = self.conv(v1) 
        v13  = v1 * 0.7978845608028654
        v14  = torch.tanh(self.conv(v9))  
        return v1


# Initializing the model