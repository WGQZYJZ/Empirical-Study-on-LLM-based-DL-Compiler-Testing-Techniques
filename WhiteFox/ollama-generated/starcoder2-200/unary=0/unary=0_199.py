
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 * 0.5  
        v3  = v1 ** 2
        v4  = v3 ** 2  
        v5  = v4 * 0.044715
        v6  = v1 + v5
        v7  = torch.tanh(v6) 
        v8  = v7 + 1    
        v9  = v2 * v8      
        return v9
