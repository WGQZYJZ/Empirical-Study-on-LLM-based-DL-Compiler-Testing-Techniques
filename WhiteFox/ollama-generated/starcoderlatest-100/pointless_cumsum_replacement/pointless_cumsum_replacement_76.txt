
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensor, arg1=50, arg2=32):
        t1 = torch.full([arg1, arg2], 1, dtype=input_tensor.dtype, layout=input_tensor.layout, device=input_tensor.device) 
        t2 = convert_element_type(t1, input_tensor.dtype) 
        t3 = torch.cumsum(t2, dim=1) 
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
