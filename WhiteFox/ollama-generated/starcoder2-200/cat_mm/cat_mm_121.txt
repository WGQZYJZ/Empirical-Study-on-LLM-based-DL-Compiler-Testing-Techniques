
class Model(torch.nn.Module):
    def __init__(self, input1=5082479):
        super().__init__()
 
    def forward(self, x1): 
        v1  = torch.mm(x1[0], x1[1])
        v2  = torch.cat([v1] * 3)
        return v2
 
# Initializing the model
m  = Model()

 # Inputs to the model
    x1  = [torch.randn(657,48), torch.randn(657, 49)]
__output__  = m(*x1)
