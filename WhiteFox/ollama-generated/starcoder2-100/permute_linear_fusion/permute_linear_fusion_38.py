
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # Use a single argument (instead of two arguments) as input to the model.
        v2 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(3) # Use a single argument instead of two arguments as input for the model

# Generating new model and input tensors
x, model  = m.generate_sample()

