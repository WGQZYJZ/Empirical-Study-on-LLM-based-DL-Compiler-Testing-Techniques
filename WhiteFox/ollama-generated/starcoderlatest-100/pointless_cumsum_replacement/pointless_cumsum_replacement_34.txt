
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.full([64, 64], 1, dtype=torch.float, layout='C', device='cuda')
        v2 = convert_element_type(v1, torch.double)
        v3 = torch.cumsum(v2, 0)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64).to('cuda')
