
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.Linear()(x1)
        v2  = (v1 > 0).float() * (-negative_slope) + ((~(v1 > 0)).float() * v1) 
        return v2

# Initializing the model
m = Model()

# Inputs to the model
input_tensor  = torch.randn(5, 4)
__output__  = m(x1)

