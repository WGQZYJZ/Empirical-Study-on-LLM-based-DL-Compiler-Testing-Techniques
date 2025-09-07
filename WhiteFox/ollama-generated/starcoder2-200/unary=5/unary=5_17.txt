
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1  *  0.5 # [3 3 4 9]
        v3  = v1  *   0.7071067811865476
        v4  = torch.erf(v3)
        v5  = v4 + 1 
        v6  = v2  *   v5 # [3 3 9 3]
        return v6
