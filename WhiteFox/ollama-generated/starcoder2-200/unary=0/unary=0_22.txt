
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1): 
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1 + (v2 ** 3) * 0.044715  
        v4  = torch.tanh(v3 * 0.7978845608028654 + 1) 
        return v4
