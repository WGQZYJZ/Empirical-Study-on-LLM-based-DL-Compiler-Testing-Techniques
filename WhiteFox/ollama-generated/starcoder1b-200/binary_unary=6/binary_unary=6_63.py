
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16, bias=False)

    def forward(self, x):
        v = self.linear(x) - 0.5
        return relu(v)


# Initializing the model
m = Model()


