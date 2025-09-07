
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        return torch.nn.functional.dropout(self.linear(x1), ...)

# Initializing the model
m = Model()

