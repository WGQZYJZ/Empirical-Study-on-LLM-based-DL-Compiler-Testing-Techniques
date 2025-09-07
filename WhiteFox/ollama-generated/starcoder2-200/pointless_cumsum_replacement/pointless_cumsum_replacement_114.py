
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.add = torch.nn.Add()
 
    def forward(self, x1, y1):
        v1  = convert_element_type(x1, dtype)
        v2  = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        v3  = v1 + v2 # Add the two tensors elementwisely
 
        return self.add(v3, y1)

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn([100, arg1], dtype=dtype, layout=layout, device=device, pin_memory=False)
y1 = torch.randn(arg2, dtype=dtype, layout=layout, device=device, pin_memory=False)

 # Calling the model with inputs to generate outputs
__output__  = m(x1, y1)

