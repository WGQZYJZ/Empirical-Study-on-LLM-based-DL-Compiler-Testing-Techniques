
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.mm(x1[0], x2) 
        return v1
 
# Initializing the model with input tensors as inputs to the model: x1 and x2
m = Model()
x1  = (torch.randn(3), torch.randn(5))
x2  = torch.randn(3, 4).long()
__output__  = m(x1)

