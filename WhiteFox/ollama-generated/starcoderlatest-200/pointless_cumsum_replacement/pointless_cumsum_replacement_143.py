
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        t1 = torch.full([x1.size(0), x2.size(-1)], 1, dtype=torch.float64, layout=torch.strided, device=x1.device, pin_memory=False)
        t2 = convert_element_type(t1, torch.float64)
        t3 = torch.cumsum(t2, 1)
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
