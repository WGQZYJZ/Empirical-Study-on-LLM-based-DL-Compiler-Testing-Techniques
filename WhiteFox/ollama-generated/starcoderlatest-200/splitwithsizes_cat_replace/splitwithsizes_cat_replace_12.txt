
class Model(torch.nn.Module):
    def __init__(self, dim = 1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        split_tensors = torch.split(v1, [0.5], dim)
        concatenated_tensor = torch.cat(split_tensors, dim = dim)
        return concatenated_tensor

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
m = Model()
output = m(x1)


