
class Model(torch.nn.Module):
    def __init__(self, num_layers: int = 3):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.relu  = torch.nn.ReLU()
        self.conv2 = torch.nn.Conv2d(8, 16, 3)
        self.linear = torch.nn.Linear(16, 2)
        self.dropout = torch.nn.Dropout2d(0.5)

    def forward(self, x):
        v = [self.conv1(x)]
        for _ in range(num_layers - 1):
            v.append(torch.cat([v[-1], v[-1]], dim=1))
            v.append(self.relu)
            v.append(self.conv2(v[-1]))
        v = self.dropout(torch.cat(v, dim=1), training=True)
        return torch.nn.functional.linear(v[-1], 2)


# Initializing the model
m = Model()


