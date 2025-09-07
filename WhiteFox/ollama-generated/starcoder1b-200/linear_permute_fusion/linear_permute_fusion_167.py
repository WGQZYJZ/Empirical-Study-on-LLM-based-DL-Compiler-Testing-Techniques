
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1  = self.linear(x1)  # Invoking the linear function on an input tensor firstly and then it swaps the last two dimensions of this tensor.
        return v1


# Initializing the model
m  = Model()


# Inputs to the model
input_tensor = torch.randn(1, 2, 3)
