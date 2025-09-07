
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(8 * 64 * 64, 10)

    def forward(self, x):
        x_ = linear(x)
        return relu(x_)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 28 * 28)
