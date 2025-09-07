
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        v1 = torch.nn.functional.conv2d(x, torch.tensor([...]), 1)
        bn = torch.nn.BatchNorm2d(v1.shape[1]) # The number of input channels depends on the tensor in x
        output = bn(v1)

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 56, 56)
