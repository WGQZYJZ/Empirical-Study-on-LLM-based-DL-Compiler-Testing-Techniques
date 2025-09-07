
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0)
        t2 = t1.view(-1, t1.shape[-1])
        t3 = torch.relu(t2)
        y = self.linear2(t3)
        return y


# Initializing the model
m = Model()
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
