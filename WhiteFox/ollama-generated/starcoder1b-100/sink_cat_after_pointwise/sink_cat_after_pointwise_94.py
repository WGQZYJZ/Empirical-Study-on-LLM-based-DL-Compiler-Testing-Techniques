
class Model(torch.nn.Module):
    def __init__(self, num_classes=2):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 3)
        self.linear2 = torch.nn.Linear(3, num_classes)

    def forward(self, x):
        v1 = torch.cat([x.view(-1), x.view(-1)], dim=1)
        v2 = torch.relu(self.linear1(v1))
        return self.linear2(v2)


# Inputs to the model
x1  = torch.randn(3, 5)
