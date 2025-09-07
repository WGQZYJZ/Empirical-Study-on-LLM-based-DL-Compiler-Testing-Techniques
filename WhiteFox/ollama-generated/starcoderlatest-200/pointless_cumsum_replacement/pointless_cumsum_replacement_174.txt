
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([x1.size()[0], 8], 1, dtype=torch.float64, device=x1.device) # Create a tensor filled with the scalar value 1, with the specified dtype and device 
        v2 = convert_element_type(v1, x1.dtype)
        v3 = torch.cumsum(v2, 1)
        return v3
# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(256, 100, 784)
