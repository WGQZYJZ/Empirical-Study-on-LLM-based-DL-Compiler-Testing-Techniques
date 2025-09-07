
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.full([x1.size()[0], x1.size()[1]], 1, dtype=x1.dtype, layout=x1.layout, device=x1.device, pin_memory=False)
        v2 = convert_element_type(v1, x1.dtype)
        v3 = torch.cumsum(v2, dim=1)
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
