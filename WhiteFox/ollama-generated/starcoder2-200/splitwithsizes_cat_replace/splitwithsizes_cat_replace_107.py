
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
    	split = torch.split(x1[0], 48, dim=3)
    	return torch.cat([t for t in split], dim=2), \
    	       torch.cat([v for v in split], dim=-2), \
    	       1


m = Model()

# Initializing the model and collecting inputs to the model
x0  = [torch.randn(3, 64) for i in range(7)]
x1 = [torch.randn(8, 64*j) for j in (2**i for i in range(5))]
 
__output__  = m(x0), x1


