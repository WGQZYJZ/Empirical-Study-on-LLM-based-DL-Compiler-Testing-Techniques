
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 50)

    def forward(self, x):
        return self.linear(x) * 0.9


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(2, 3, 64, 64)
