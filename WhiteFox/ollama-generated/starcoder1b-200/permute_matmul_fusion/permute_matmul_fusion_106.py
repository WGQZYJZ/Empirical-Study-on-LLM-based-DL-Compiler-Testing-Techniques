
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = self.linear1(v1)  # Linear transformation to the permuted tensor A
        v3 = self.linear2(v2)  # Linear transformation to the permuted tensor B
        return v3


# Initializing the model
m = Model()


