
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
        self.layers = torch.nn.ModuleList([
            torch.nn.Linear(dim, dim), # The input to the first layer should be dim
            torch.nn.ReLU(),
            torch.nn.Linear(dim, dim)  # The output of the second layer should be dim
        ])

    def forward(self, x):
        output = x
        for layer in self.layers:
            output = layer(output)
        return output


# Initializing the model
m = Model(16)


# Inputs to the model
x = torch.randn(3, 2, 15, 10)
