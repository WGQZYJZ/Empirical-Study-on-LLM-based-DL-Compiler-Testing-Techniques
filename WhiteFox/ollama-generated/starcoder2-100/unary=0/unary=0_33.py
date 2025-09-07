
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1 ** 2
        v4  = v1 ^ v3 
        v5  = torch.div(v3 + .798, (v1  * 1))
        v6  = v4 * (.54) 
        v7  = v5  +  0.879942
        v8  = v2  * v7 
        return v8
