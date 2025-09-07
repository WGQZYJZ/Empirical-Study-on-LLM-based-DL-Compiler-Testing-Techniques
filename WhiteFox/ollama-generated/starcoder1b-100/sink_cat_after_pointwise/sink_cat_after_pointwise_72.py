
class Model(torch.nn.Module):
    def __init__(self, num_layers: int = 2):
        super().__init__()

        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

        self.relu = torch.nn.ReLU()
        self.stack = []
        for i in range(num_layers):
            self.stack.append(torch.nn.ReLU())

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)

        # Reshape
        v2 = torch.cat([v1, v1], dim=1)

        # Linear
        for i in range(len(self.stack)):
            v3 = self.relu(v2.view(-1, 4))
            v2 = self.linear1(v3)
            if i < len(self.stack) - 1:
                v3 = self.stack[i](v2)
                v2 = self.linear2(v3)

        return v2


# Initializing the model
m = Model()
