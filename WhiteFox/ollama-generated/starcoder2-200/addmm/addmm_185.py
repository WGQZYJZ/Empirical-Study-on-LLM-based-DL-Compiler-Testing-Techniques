
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2, inp):
        v1 = torch.mm(input1, input2) 
        v2  = v1 + inp
        return v2

 # Initializing the model
m = Model()
 
# Inputs to the model (x and y are tensors; inp is not a tensor but is keyword argument in forward method of torch.nn.Module class.)
x  = torch.randn(4, 3)  
y  = torch.randn(5, 3)  

__output__  = m(x, y, x)

