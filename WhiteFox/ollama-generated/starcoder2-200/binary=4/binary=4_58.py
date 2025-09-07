
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 1568 + 4096, 1)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = v1 + other
        return self.relu(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(32, 1568)
other = torch.rand(4096) * 7 - 1e-2
x2 = other + x1 # The input tensor is not equal to zero


# Initializing the model
m = Model()
__output__  = m(x1, other)

The output tensor is different from the input.