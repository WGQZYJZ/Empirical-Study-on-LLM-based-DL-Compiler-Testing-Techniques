
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v0   = torch.full([5, 4], 1, dtype=torch.float64)  # Create a tensor filled with the scalar value 1
        v1   = torch.convert_element_type(v0, torch.float32) 
        v2   = torch.cumsum(v1, dim=-1).view(-1, 5) 
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(500, 784)
__output__  = m(x1)

