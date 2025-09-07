
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1   = self.conv(x1)
        v2   = v1 * 0.5
        v3   = v1 ** 2 
        v4   = v1 ** 3
        v5   = torch.tensor([v4], device="cuda:0")
        v6   = torch.tensor([v5], device="cuda:0") * 0.044715
        v7   = v1 + v2 + v6 
        v8   = torch.tensor([v7], device="cuda:0") * 0.7978845608028654
        v9   = v7 / v3 
        v10  = -2 * (v9 ** (-1)) + 1
        v11  = v8 + torch.tensor([x], device="cuda:0")
        return x


# Initializing the model
m  = Model()

 # Inputs to the model
x   = torch.randn(5, 3, 64, 64)
 
__output__  = m(x)