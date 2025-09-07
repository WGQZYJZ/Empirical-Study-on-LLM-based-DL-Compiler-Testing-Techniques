
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1) # Apply the linear transformation to an input tensor
        return relu(v1 - other), v1

# Initializing the model
m = Model()
other = torch.randn((10,))  # A random value between [-3.4652, ..., 8.791]

# Inputs to the model
x1 = torch.randn(10)
v1, v2 = m(x1)

