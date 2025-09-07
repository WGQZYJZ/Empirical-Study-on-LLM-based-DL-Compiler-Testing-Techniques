
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, arg1=50, arg2=""):
        v1 = torch.full([arg1, arg2], 1, dtype=x1.dtype, layout=x1.layout, device=x1.device)
        v2 = convert_element_type(v1, x1.dtype)
        v3 = torch.cumsum(v2, 1)
        return v3
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(50, dtype=torch.float)
