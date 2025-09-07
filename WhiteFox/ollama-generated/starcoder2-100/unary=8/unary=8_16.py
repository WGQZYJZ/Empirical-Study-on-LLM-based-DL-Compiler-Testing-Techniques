
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = v1 + 3
        v3  = torch.clamp(v2, min=0)
        v4  = torch.clamp(v3, max=6)
        v5  = v1 * v4
        v6  = v5 / 6
        return v6


# Initializing the model with a randomly generated value for the tensor
m = Model()
 
x1  = torch.randn([20])
__output__  = m(x1)