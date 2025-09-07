
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.full([x1], 1, dtype=x2)
        v2 = convert_element_type(v1, x2)
        v3 = torch.cumsum(v2, dim=1)
        return v3
# Initializing the model
m = Model()

# Inputs to the model
x1 = 4
x2 = torch.float64
