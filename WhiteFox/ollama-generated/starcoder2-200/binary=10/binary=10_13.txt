
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=None):
        v1 = torch.nn.functional.linear(x1)
        v2 = v1 + other # other is added to the output of the linear transformation
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model (other will be randomly generated for each execution)
x1, other = torch.randn(3,5), torch.randn(3,5)
 
 __output__  = m(x1, other=other)