
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.dim  = dim
 
    def forward(self, x1):
        v1  = torch.addmm(x1, torch.randn(32768*4), torch.randn(4, 32768))
        return torch.cat([v1], self.dim)

# Initializing the model
m  = Model()
 
# Inputs to the model
input_tensor = torch.rand(50000, 32768)
__output__   = m(input_tensor)

