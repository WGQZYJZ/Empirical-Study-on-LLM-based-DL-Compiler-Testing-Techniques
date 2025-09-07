
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.full([1], 1)
        v2  = convert_element_type(v1, dtype)
        v3  = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 5, 64)
x2 = torch.randn(1, 2, 64, 5)
