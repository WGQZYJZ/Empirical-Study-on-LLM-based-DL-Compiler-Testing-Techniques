
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 10)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other # <- 'other' is a certain value that you specify (for example, 57.6849)
        v3 = torch.nn.functional.relu(v2)

        return v3

# Initializing the model
m = Model()

