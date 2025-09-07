
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.Linear(32, 64)(x1)
        v2  = v1 > 0
        v3  = negative_slope * v1
        v4  = torch.where(v2, v1, v3)
        return v4

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(16, 32)

 # Model outputs for each input tensor
__output_1__  = m(x1)

