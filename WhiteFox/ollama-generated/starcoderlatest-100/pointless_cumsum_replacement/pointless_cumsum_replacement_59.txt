
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.t1 = torch.full([8, 32], 1, dtype=torch.float, layout=torch.strided, device="cuda:0", pin_memory=False)
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.t1 * torch.ones([8, 32], dtype=torch.float, layout=torch.strided, device="cuda:0", pin_memory=False)
        v2 = convert_element_type(v1, "float")
        v3 = torch.cumsum(v2, 1)
        v4 = self.conv(x1)
        return v4


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
