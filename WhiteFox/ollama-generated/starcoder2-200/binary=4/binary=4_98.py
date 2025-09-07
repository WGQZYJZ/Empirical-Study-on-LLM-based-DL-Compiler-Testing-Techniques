
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other):
        v1 = torch.nn.functional.linear(x1) 
        v2  = v1 + other
        return v2

 # Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1024,)
other  = torch.randn(1024,) 
 
# Output of the model (no need for __output__ here because this example doesn't need it)
__output__  = m(x1, other)