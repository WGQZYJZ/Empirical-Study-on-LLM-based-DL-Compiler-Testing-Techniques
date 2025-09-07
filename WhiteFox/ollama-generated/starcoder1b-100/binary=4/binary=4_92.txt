
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(200, 5)

    def forward(self, x):
        v1 = self.linear1(x) + x # Add x to the output of the linear transformation
        return v1


# Initializing the model
m = Model()

