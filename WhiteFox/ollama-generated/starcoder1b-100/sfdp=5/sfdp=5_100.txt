
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(1, 10)
        self.fc2 = torch.nn.Linear(10, 10)

    def forward(self, x):
        # The size of a linear layer is the number of inputs it takes in and outputs one or more values. It should be noted that `F.linear` takes the input into consideration while the `input_dropout` is performed only on the last output.
        x = self.fc1(x)  # Compute a linear transformation of the input, which can be done with a linear layer and then the dropout operation will not impact the output from a single linear layer anymore.
        x = F.linear(x, self.fc2, None)  # The second argument is a bias vector that represents a fixed amount added to every linear element in the result. A bias vector can be specified in the `Linear` class as a parameter of the constructor, or as an argument to the `linear` method with a name starting with `bias`.
        x = F.relu(x)  # Apply ReLU to the computed linear transformation to enforce the non-negative element on the result
        return x

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
