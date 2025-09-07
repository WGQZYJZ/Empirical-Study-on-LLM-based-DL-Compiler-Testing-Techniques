
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([1, 4], 0, dtype=x1.dtype, layout=x1.layout, device=x1.device, pin_memory=False) 
        return convert_element_type(torch.cumsum(v1, 1), x1.dtype)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64).to(device)
