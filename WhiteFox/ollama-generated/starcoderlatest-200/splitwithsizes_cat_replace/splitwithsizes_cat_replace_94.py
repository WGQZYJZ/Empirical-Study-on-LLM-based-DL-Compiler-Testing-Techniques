
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 4, 1, stride=1, padding=1)
 
    def forward(self, x1):
        s1, t1, u1 = torch.split(x1, split_sizes=[64, 64, 64], dim=-2) # split into three tensors along the 2nd dimension of input tensor
        c1 = torch.cat([s1, t1], dim=-2) # concatenate two tensors in the same dimension 
        v = self.conv1(c1)
        return v

# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(3, 64, 64)
