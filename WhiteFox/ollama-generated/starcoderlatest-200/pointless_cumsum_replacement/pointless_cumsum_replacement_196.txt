
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([3, 64, 64], 1, dtype=torch.float, layout=torch.strided, device=x1.device, pin_memory=False)
        v2 = convert_element_type(v1, torch.float)
        v3 = torch.cumsum(v2, 1)
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64).to('cuda')
