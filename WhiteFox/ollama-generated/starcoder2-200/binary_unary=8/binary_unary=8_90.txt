

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)

        v2 = v1 + other # <--- this tensor is used to model 'other'
        v3 = torch.relu(v2)
        return v3

# Initializing the model with a different input and different output tensor 
m = Model()
x1, v4 = torch.randn(1, 3, 64, 64), torch.randn(1, 8, 59, 59) # <--- the values of the tensors are randomly generated for the example
output = m(x1)
assert output == v4
