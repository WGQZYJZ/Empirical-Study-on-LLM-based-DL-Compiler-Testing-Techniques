
class Model(torch.nn.Module):
    def __init__(self, num_features: int, num_linear_units: int):
        super().__init__()
        self.linear1 = torch.nn.Linear(num_features, num_linear_units)
        self.activation = torch.nn.ReLU()

    def forward(self, x1):
        linear_result = self.linear1(x1)
        return self.activation(linear_result + other)


# Initializing the model
m = Model(__num_features__, __num_linear_units__)


# Inputs to the model
x1  = torch.randn(1, 8)
