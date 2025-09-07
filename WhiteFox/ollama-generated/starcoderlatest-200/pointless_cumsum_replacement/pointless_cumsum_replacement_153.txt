
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t1 = torch.full([64, 64], 1, dtype=x1.dtype, layout=x1.layout, device=x1.device)
        t2 = convert_element_type(t1, x1.dtype)
        t3 = torch.cumsum(t2, 1)
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 64, 64).to(torch.float32)
