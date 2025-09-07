
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1):
        v1  = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False) 
        v2  = convert_element_type(v1, dtype)
        v3  = torch.cumsum(v2, 1) # Compute the cumulative sum of the elements of the tensor along dimension `1`
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
arg1  = torch.randint(-800, 800,(1,))
arg2  = torch.randint(16,48,(1,))
__output__  = m(arg1)