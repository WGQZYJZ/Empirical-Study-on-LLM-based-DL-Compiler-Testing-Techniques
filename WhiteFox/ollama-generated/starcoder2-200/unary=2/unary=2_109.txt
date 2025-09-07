

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = v1 * 0.5
        v3  = (v1 ** 3) * 0.044715
        v4  = v1 + v3
        v5  = v4 * 0.7978845608028654
        v6  = torch.tanh(v5)
        v7  = v6 + 1
        v8  = v2 * v7
        return v8


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(3, 4, 90, 90)
__output__  = m(x1)

