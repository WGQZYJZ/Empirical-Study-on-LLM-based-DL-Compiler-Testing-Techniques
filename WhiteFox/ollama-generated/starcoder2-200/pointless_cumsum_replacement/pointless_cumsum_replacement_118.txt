
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = convert_element_type(v1, dtype=v1.dtype)
        return torch.cumsum(v2, 1)


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(305447981, 3, 64, 64)
