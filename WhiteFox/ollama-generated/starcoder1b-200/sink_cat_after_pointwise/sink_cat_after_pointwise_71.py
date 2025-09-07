
class Model(torch.nn.Module):
    def __init__(self, num_layers=1):
        super().__init__()
        self.fc = torch.nn.Linear(...)
        self.relu  = torch.nn.ReLU()

    def forward(self, x):
        x  = x.permute(0, 2, 1)
        x  = self.fc(x)
        x  = self.relu(x)
        return x


# Initializing the model
m = Model()

