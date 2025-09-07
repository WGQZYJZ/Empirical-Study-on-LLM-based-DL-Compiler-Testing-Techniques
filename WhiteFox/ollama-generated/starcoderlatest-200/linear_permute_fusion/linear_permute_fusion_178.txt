
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1,  self.linear.weight, self.linear.bias) # Apply linear transformation to the input tensor.
        v2 = v1.permute(0, 2, 1) # Permute the output tensor from the linear transformation.
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 10, 4)
