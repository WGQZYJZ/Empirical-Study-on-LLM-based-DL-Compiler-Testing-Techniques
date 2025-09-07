
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2) # Matrix multiplication of two input tensors 
        v2  = torch.cat([v1] * 4 + [v1], dim=0) # Concatenation along dimension 0 with a repetition
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
x1, x2 = torch.randn(32), torch.randn(8)
__output__  = m(x1, x2)
 
