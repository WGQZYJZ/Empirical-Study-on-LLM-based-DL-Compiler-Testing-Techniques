
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 3)

    def forward(self, x1):
        t1 = x1.view(-1, 1).permute(0, 2, 1)  # Flatten input to 1 dimension
        return self.linear(t1)

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 3)
