
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        t1 = torch.full([x1.shape[0], x1.shape[1]], 1, dtype=torch.float32, layout=torch.strided, device=x1.device)
        v1 = self.conv(x1)
        v2 = convert_element_type(v1, torch.float32)
        t2 = torch.cumsum(v2, 1)
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
