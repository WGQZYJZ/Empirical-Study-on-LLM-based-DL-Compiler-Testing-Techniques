
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, inplace=True)
        v2 = torch.nn.functional.dropout(v1 + 100.) # This line is used as an example of input dependency.
        return v2


# Initializing the model