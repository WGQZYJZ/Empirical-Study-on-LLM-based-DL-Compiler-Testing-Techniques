
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.full([x1.size()[0], 4, 32, 32], 1)
        v2 = convert_element_type(v1, dtype=x1.dtype)
        v3 = torch.cumsum(v2, 1)
        return v3
 
# Initializing the model and inputs to the model
m = Model()
x1 = torch.randn(4, 3, 64, 64)
x2 = 8
