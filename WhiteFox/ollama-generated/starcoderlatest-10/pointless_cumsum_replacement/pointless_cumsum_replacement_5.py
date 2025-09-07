
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.full([3], 1, dtype=torch.float)
        v2 = convert_element_type(v1, x2)
        v3 = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m = Model()
x1 = torch.randn(10, dtype=torch.float)
x2 = torch.randint(5, ()).item()
