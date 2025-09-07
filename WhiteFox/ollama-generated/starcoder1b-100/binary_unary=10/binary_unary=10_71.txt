
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x1):
        v1 = self.linear(x1) + 0.25 * torch.rand_like(v1) # Linear transformation and addition of a randomness
        return v3  # Return the output of ReLU activation function


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 8, 64, 64)
