
class Model(torch.nn.Module):
    def __init__(self, minv=0, maxv=5):
        super().__init__()
        self.linear = torch.nn.Linear(8*8, 2)
    
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, minv)
        v3 = torch.clamp_max(v2, maxv)
        return v3
# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(50*49 ,8*8)
__output__= m(x1)

 