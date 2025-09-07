
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1)
 
    def forward(self, x1):
        v1   = self.conv(x1) 
        v2  = v1 * 0.5              # (3, 64, 64)
        v3 = v2  * v2  * v2          # (3, 64, 64)
        v4 = v3   * 0.044715         # (3, 64, 64)
        v5 = v1 + v4                 # (3, 64, 64)
        v6 = v5*v2                   # (3, 64, 64)
        v7 = torch.tanh(v6)           # (3, 64, 64)
        v8 = v7 +1                    # (3, 64, 64)
        