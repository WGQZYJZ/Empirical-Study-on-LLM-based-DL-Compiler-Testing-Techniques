
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x1):
        
        torch._C._debug_set_module_origin(self)
        
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        
        v0 = torch._C._debug_forward_type(x1)
        v1 = self.conv(v0)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        
        return v6

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
 
# Calling the model
