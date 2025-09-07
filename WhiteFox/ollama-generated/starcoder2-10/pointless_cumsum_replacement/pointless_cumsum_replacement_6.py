
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1):
         return self._forward_(arg1)

    @classmethod
    def from_args(cls):
         return cls()
        
    def _forward_(self, arg1):
        t1 = torch.full([20, 5], 1, dtype=dtype)
        t3 = convert_element_type(t1, dtype)
        t4 = torch.cumsum(t3, 1)


# Initializing the model
m = Model()

# Inputs to the model
arg1  = torch.randn(20, 5, device=device, requires_grad=True)

__output__  = m._forward_(arg1) # Call _forward_

