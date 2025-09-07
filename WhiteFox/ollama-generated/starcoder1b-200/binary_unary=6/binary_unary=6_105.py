
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 32, bias=True)

    def forward(self, x1):
        v1 = self.linear(x1) - 0.1
        return v1


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(2, 32)
