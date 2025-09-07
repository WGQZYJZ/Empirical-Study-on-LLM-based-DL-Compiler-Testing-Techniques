
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(...) # X can be 1, 2 or 3 representing the dimension

    def forward(self, x1):
        bn1 = torch.nn.functional.batch_norm(...)
        out = torch.nn.functional.conv1d(bn1(...), self.conv)
        return out


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 4096) # X can be 1, 2, or 3 representing the dimension
