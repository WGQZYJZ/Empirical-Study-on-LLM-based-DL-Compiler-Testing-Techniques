
class Model(torch.nn.Module):
    def __init__(self, d_in: int = 3, d_hid: int = 128):
        super().__init__()
        self.fc = torch.nn.Linear(d_in, d_hid)
        self.activation = torch.nn.ReLU()

    def forward(self, x: torch.Tensor):
        return self.activation(self.fc(x))

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(10, 3)
