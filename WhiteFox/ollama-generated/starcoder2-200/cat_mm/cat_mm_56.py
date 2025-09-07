
class Model(torch.nn.Module):
    def __init__(self, input1=None, input2=None):
        super().__init__()
        self.mm = torch.mm
    
    def forward(self, x1, x2):
        v1  = self.mm(x1, x2) 
        v2  = torch.cat([v1 for i in range(3)], dim=-1)
        return v2

# Initializing the model
m = Model()
__output__  = m(x1=torch.randn(8), x2=torch.randn(9))