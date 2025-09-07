
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([x1.shape[0], x1.shape[1]], 1, dtype=x1.dtype, device=x1.device) 
        v2 = convert_element_type(v1, x1.dtype)
        v3 = torch.cumsum(v2, 1)  
        return v3

 # Initializing the model
m = Model()
 
 # Inputs to the model
x1 = torch.randn(4, 5, dtype=torch.float32)
