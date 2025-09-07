
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2048, 512)

    def forward(self, x):
        return self.linear1(x + 1)


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(1, 2048)
