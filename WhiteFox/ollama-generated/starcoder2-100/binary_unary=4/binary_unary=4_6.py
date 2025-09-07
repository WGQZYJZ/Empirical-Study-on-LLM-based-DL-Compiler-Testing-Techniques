
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v = torch.nn.functional.linear(x1) 
        v  += other # Pass a keyword argument `other` as the input to the function `linear`
        v = torch.relu(v)
 
        return v


m  = Model()
 
x2 = torch.randn(3,4,5,6)
__output__= m(x1, other=x2)