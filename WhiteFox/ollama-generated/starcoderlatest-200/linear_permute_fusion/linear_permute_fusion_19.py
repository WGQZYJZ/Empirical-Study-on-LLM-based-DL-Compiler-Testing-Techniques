
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 10)

    def forward(self, x):
        v1 = torch.nn.functional.linear(x, self.linear.weight, self.linear.bias) # Apply linear transformation on the input tensor
        v2 = v1.permute(0, 2, 1) # Permute the output tensor of the linear transformation
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 2, 3, 4)
