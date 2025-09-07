
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        return torch.nn.functional.dropout(x1, p=0.)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
