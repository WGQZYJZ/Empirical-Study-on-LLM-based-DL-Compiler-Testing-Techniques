
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = convert_element_type(v1, torch.float64) * 0.5
        v3 = convert_element_type(v1, torch.float64) * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return convert_element_type(v6, torch.float64)


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
