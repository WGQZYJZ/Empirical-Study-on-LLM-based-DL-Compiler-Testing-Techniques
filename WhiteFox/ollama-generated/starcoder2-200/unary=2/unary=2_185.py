
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v2 ** 3 
        v4  = torch.tensor([0.044715])
        v6  = v3 + v4 
        v7  = v2 + v6
        v8  = torch.tensor([0.7978845608028654])
        v9  = v7 * v8 
        v10 = torch.tanh(v9)
        v13 = torch.tensor([1.0])
        v14 = v10 + v13 
        return v2 * v14

