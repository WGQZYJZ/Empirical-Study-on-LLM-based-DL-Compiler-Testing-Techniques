
class Model(torch.nn.Module):
    def __init__(self, hidden_size: int):
        super().__init__()
        self.fc1 = torch.nn.Linear(4 * 4 * 3, hidden_size)
        self.fc2 = torch.nn.Linear(hidden_size, 10)

    def forward(self, x):
        h = x.view(-1, 4 * 4 * 3).contiguous()
        h = self.fc1(h)
        return F.log_softmax(self.fc2(h))


# Initializing the model
m = Model(hidden_size=10)


# Inputs to the model
x1 = torch.randn(1, 4 * 4 * 3)
