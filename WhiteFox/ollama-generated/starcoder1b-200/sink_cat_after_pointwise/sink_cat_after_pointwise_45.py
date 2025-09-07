
class Model(torch.nn.Module):
    def __init__(self, num_layers=1):
        super().__init__()

        self.linear = torch.nn.Linear(...)
        ...

    def forward(self, x1, *args):  # Pass an input tensor to the first hidden layer of this model.
        v1 = self.linear(x1)
        return v1


# Initializing the model
m = Model()
x1 = torch.randn(1, 2, 2)
