
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*64*3, 10)

    def forward(self, x):
        y = self.linear(x)
        z = relu(y)
        return z


# Initializing the model
m = Model()


