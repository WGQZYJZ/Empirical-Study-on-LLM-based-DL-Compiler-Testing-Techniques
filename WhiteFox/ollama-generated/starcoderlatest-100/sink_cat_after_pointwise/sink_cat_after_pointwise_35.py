
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0)
        t2 = t1.view(t1.shape[0]*t1.shape[1], -1)
        t3 = torch.nn.functional.relu(t2)
        return self.linear(t3)


# Inputs to the model
x1 = torch.randn(4, 2)
x2 = torch.randn(8, 2)
