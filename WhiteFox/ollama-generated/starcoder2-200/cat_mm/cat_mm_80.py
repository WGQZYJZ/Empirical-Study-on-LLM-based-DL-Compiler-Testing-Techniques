
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
        
    def forward(self, input1, input2):
        v1  = torch.mm(input1, input2) 
        v2  = torch.cat([v1 for i in range(len(v1))], dim=0)
        return v2

# Initializing the model
m  = Model(torch.randn(4), torch.randn(3))
 
# Inputs to the model
x1, x2  = (torch.randn(5), torch.randn(7))
 
__output__  = m(x1, x2)

