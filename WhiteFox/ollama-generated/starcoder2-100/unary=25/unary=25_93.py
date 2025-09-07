
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.functional.linear(x1)
        v2  = v1 > 0
        v3  = v1 * -v2
        v4  = torch.where(v2, v1, v3)
        return v4


# Initializing the model and setting the negative slope to 5 for testing purposes:
m = Model()
negative_slope = 5
 
# Inputs to the model:
x1 = torch.randn(1, 784)
__output__  = m(x1)


