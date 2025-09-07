
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other):
        v1 = self.conv(x1)
        return v1 + other


# Initializing the model
m = Model()
other_tensor = torch.randn(3, 8, 64, 64)
__output__  = m(input_tensor, other=other_tensor)

