
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.lin   = torch.nn.Linear(64 * 64 * 8, 500)
    
    def forward(self, x1):
        v1  = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        v2  = convert_element_type(v1, dtype)
        v3  = torch.cumsum(v2, 1)
        v4  = self.conv(x1) 
        v5  = self.lin(v4.reshape(-1))  
        return v5

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(arg3, arg4, 64, 64)
