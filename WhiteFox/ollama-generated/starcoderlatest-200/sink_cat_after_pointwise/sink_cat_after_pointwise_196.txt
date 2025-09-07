
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=-1)
        t2 = t1.view(-1, 2)
        t3 = torch.relu(t2)
        return self.linear(t3).squeeze()


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 2, 5)
x2 = torch.randn(1, 2, 6)
