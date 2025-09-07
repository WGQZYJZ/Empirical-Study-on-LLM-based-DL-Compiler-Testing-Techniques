
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(64*64*3, 8)

    def forward(self, x):
        v = self.fc1(x)
        return relu(v)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 64, 64, 3)
