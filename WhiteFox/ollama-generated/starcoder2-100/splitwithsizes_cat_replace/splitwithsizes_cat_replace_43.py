
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.split(x1, 32, dim=0)
        v4 = [v for i in range(len(v2)) if i % 2 == 0] 
        v5 = [torch.cat(v4)]
        return v5
 
# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(3, 8, 64, 96)
__output__  = m(x1)


