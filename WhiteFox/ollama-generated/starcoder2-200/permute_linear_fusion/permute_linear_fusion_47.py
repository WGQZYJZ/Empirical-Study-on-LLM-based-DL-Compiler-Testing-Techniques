class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        # Initialize self.linear
        self.linear = torch.nn.Linear(2, 2)

        return x1


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3)

