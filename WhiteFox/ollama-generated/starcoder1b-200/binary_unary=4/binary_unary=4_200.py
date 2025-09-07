
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 8)

    def forward(self, x):
        v = self.linear(x) + 5  # Add a number `5` to the output of the linear transformation
        return relu(v)


# Initializing the model
m = Model()

