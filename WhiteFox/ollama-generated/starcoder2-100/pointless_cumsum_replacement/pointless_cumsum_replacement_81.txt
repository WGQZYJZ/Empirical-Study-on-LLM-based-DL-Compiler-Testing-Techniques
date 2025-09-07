
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        v1  = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        v2  = convert_element_type(v1, dtype)
        v3  = torch.cumsum(v2, 1) # __output__
        return v3


# Initializing the model<|end_of_model|>
m = Model()

# Inputs to the model<|end_of_input|>
arg1  =  4096
arg2  =  512
__output__  = m(arg1, arg2)