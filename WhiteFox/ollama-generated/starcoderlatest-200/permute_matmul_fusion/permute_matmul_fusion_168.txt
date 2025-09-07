
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 4)
        self.linear2 = torch.nn.Linear(4, 8)
        self.linear3 = torch.nn.Linear(8, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # permute tensor A to be of shape (1, 4, 2)
        v2 = self.linear1(v1)    # linear transformation on tensor B to be of shape (1, 8, 4)
        v3 = self.linear2(v2)    # linear transformation on tensor C to be of shape (1, 2, 8)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 4, 2)
