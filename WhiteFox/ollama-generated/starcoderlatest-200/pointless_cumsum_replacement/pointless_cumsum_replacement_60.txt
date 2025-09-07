
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.full([x1.shape[0], x1.shape[1]], 1, dtype=torch.float32, layout='NCHW', device=x1.device, pin_memory=False)
        v2 = convert_element_type(v1, torch.dtype)
        v3 = torch.cumsum(v2, 1)
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
