
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v1 = torch.mm(x1, x2)
        return v1 + inp
 
m  = Model()

 # Initializing the model with two input tensors: 'inp' and 'x2'.
inp  = torch.randn(30768,)
x2  = torch.randn(59442, 59442)
# Assigning 'inp' to be the  keyword argument of method `forward()` on `m`.
m._modules['forward'].inp  = inp

# Inputs to the model: two tensors - 'x1', and 'x2'.
x1 = torch.randn(30768,59442)

