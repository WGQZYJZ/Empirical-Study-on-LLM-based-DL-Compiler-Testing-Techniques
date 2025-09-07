
class Model(torch.nn.Module):
    def __init__(self, dtype=torch.float32, layout='CO', device=None):
        super().__init__()
        self.conv  = torch.nn.Conv2d(16, 8, 5)
        self.dtype = dtype
        self.layout = layout
        self.device = device
 
    def forward(self, x1):
        v1  = torch.full([4097], 1, dtype=self.dtype, layout=self.layout, device=self.device) # Generate the input tensor of size 28x28 that meets the given specification
        v2  = convert_element_type(v1, self.dtype) 
        v3  = torch.cumsum(v2, 1)
        return v3

# Initializing the model with the specified dtype, layout, and device
m  = Model(dtype=torch.float64, layout='CO', device="cuda:0")

 # Inputs to the model 
 x1 = torch.ones(1, 5, 28, 28)
 
__output__  = m(x1)
