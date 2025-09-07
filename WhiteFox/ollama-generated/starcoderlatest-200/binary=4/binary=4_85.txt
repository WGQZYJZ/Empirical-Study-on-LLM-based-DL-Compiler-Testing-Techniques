
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(256, 1)
 
    def forward(self, x1, other):
        v1 = self.conv(x1) + other
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = torch.zeros_like(x1[0]) # [0] selects the first element of an n-D tensor. For example, when "x1" is a matrix, "x1[0]" means selecting the first row. The output shape should be (1, 8, 64, 64).
