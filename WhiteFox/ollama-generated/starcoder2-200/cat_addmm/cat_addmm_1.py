
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()

        self.linear1 = torch.nn.Linear(784, 5)
        self.linear2 = torch.nn.Linear(3*5 + 5, 5)
        self.linear3 = torch.nn.Linear(79*5, 5)

    def forward(self):

        self.linear1()

        self.linear2()

        self.linear3()

# Initializing the model