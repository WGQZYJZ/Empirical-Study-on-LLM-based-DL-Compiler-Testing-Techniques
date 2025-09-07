
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.conv2d(x1)
        v3 = v1 + torch.sum(v1 * v1, dim=0, keepdim=True).pow(3)* 0.044715
        v6 = (torch.tanh((v3* 0.7978845608028654) + 1)) * v2
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

