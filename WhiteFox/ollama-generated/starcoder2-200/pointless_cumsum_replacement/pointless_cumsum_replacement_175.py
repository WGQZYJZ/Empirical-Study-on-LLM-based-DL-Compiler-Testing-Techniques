
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.func = lambda x: torch.cumsum(x, 1)
 
    def forward(self, arg0):
        v0  = torch.full([arg0], 1, dtype=torch.float32, layout=torch.strided, device="cpu", pin_memory=False) # Create a tensor filled with the scalar value 1 and the specified dtype in the argument "arg0"
        v0 = convert_element_type(v0, torch.float64) 
        return self.func(v0)

# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = [3]
