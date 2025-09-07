
class Model(torch.nn.Module):
    def __init__(self, layer1, layer2):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

        self.layer1 = layer1
        self.layer2 = layer2

    def forward(self, x1):
        v1 = self.layer1(x1)
        v2 = self.layer2(v1)
        return v2


# Initializing the model
m = Model(torch.nn.Linear(2, 2), torch.nn.ReLU())


