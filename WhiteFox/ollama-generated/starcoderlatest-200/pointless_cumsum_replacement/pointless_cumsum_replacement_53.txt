
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([x1[0].shape[0], 1, x1[0].shape[2], x1[0].shape[3]], 1)
        v2 = convert_element_type(v1, dtype)
        v3 = torch.cumsum(v2, dim=1)
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = (torch.randn(1, 3, 64, 64), torch.float)
