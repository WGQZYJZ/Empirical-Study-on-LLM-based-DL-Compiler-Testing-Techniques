

class Model(torch.nn.Module):
    def __init__(self,  n):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1, v2 = torch.split(x1, 64, dim=3)

        v5_splitted, v7_splitted = torch.split(v2[::-1], [n-int((8+n)/2), n - int((8+n)/2)])
        v9_concatenated, v0 = torch.split([torch.cat([v3, v4]) for v3 in (v5_splitted + 1) for v4 in (v7_splitted + 1)], [1] * n * 8, dim=0)
        v9 = self.conv(x1)

        v6  = v2[::2][0] * v9
        v11 = torch.erf(v5_splitted[::-1][int((len(v7_splitted)+n)/2)])
        return [v1, v13] + list(v8)

# Initializing the model
m  = Model(4096)

 # Inputs to the model
x1  = torch.randn(5 * 3 * 64 ** 2)

 