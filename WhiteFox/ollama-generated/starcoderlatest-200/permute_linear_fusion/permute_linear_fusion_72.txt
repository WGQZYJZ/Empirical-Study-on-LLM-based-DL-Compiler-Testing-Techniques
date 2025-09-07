
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias) # linear function should be invoked with weight and bias

        v2 = torch.nn.functional.transpose(v1, 0, 1)   # Transpose the tensor.
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 2, 2)
