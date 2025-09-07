
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 10)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.1, training=True)
        v2 = self.linear(v1) # Add a linear layer to this input and then apply dropout to the result.
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 50)
