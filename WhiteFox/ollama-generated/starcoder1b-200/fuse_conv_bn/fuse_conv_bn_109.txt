
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x):
        return self.linear(x)


# Inputs to the model
inputs = ... # Permute and input to the module's forward method
outputs = Model()(inputs)


