
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=1)  # [batch_size * batch_size]
        v2 = torch.relu(v1)  # [batch_size * batch_size]
        v3 = self.linear(v2)  # [batch_size * batch_size]
        return v3


# Initializing the model
m = Model()


