
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = convert_element_type(v1, dtype) * 0.5
        v3 = convert_element_type(v1, dtype) * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = convert_element_type(v2, dtype) * v5
        return v6


# Initializing the model
m = Model()

