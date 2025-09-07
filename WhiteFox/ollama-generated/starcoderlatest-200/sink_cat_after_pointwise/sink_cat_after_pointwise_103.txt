
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1).view(10) # [45]
        v2 = torch.relu(v1)
        return self.linear(v2)


# Initializing the model and optimizer
m = Model()
opt = optim.SGD(m.parameters(), lr=0.1, momentum=0.9)

# Inputs to the model
x1 = torch.randn(4, 3)
x2 = torch.randn(4, 5)
y_true = x1 + x2 # [5, 6]
