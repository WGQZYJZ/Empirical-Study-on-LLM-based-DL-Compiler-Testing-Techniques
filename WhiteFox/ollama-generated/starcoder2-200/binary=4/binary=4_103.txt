
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other):
        v1 = torch.nn.Linear()(x1)
        v2 = v1 + other
        return v2
 
# Initializing the model with different input tensors and additional arguments for the forward method
m  = Model()
 
# Inputs to the model that are different from those used in the previous example
x1 = torch.randn(3, 10)
other_tensor = torch.randn(1, 5)
__output__   = m(x1, other=other_tensor)

