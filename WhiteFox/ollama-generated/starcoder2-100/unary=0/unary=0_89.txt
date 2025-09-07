
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 * 0.5  
        v3  = v1 **  3
        v4  = v3 + t1 * (v2 * t1  * t1 + v1) * 0.7978845608028654 * 0.044715
        v6  = torch.tanh(v4)  
        return v6
