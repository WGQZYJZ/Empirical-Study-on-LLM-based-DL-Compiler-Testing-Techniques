
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1 + self.other


# Initializing the model and passing the "other" tensor as a keyword argument to its addition operation: m(x1, other=other_tensor)
m = Model()
other_tensor  = torch.randn([32])

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1, other=other_tensor)

