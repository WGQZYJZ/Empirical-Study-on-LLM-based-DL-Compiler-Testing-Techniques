
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(16384, 512)

    def forward(self, x):
        y = self.fc(x).relu()
        return y


# Initializing the model
model = Model()

# Inputs to the model
inputs = torch.rand((1024,)) # A vector of random numbers with a size of 1024
