
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        return torch.nn.functional.relu(torch.nn.functional.dropout(x1, 0.5))


# Initializing the model
m = Model()

