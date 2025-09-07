
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3208, 100)
 
    def forward(self, x1):
        v1 = self.linear(x1) - 1  # Subtracting 1 from the output of a linear transformation
        v2 = relu(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3208)
