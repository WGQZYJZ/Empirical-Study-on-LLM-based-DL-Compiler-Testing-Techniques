
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t1 = torch.full([50, 64], 1., dtype=x1.dtype)
        t2 = torch.ops.aten.convert_element_type.default(t1, dtype="double")
        t3 = t2 + torch.cumsum(t2, dim=1)
        return t3

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(50, 64).to("cpu").half().requires_grad_(True)
 
# The output of the model
m(x1)


