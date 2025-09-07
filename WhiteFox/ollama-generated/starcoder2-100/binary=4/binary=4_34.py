
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v = torch.nn.Linear(8,32)
        v1  = v(x1) 
        v2  = v1 + other # Replace "other" with another tensor. The shape of this tensor should be the same as the output of the linear transformation.
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 8)
 
__output__  = m(x1)
