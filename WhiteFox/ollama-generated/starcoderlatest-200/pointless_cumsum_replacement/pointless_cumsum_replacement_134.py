
class Model(torch.nn.Module):
    def __init__(self, dim=3):
        super().__init__()
        self.t1 = torch.full([dim], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
 
    def forward(self, x2):
        v1 = convert_element_type(self.t1, dtype)
        v2 = torch.cumsum(v1, 1)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1, 3, 64, 64)
