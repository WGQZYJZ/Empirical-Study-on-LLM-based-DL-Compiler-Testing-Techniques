
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 4, 1, stride=1, padding=1)
 
    def forward(self, x):
        return self.conv1(x), self.conv2(x).squeeze(dim=-2)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output_1, __output_2 = m(x1)

