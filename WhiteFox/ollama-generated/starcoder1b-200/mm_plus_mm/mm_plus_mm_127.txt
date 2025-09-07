
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Linear(3, 6)
        self.m2 = torch.nn.Linear(3, 6)

    def forward(self, x1, x2):
        v1 = torch.mm(x1, self.m1)  # Matrix multiplication between input1 and weights
        v2 = torch.mm(x2, self.m2)  # Matrix multiplication between input2 and weights
        return v3 + v4  # Addition of the results of the two matrix multiplications


# Initializing the model
m = Model()


