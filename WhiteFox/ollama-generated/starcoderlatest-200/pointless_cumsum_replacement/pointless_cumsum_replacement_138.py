
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1 = torch.full([x1.size()[0], 8, x1.size()[2]], 1, dtype=dtype)
        v2 = convert_element_type(v1, dtype)
        v3 = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(16, 4, 32, 32)
x2 = x1.shape[0] // 8
