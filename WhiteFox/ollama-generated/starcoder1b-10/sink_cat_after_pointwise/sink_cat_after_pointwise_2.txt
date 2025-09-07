
class Model(torch.nn.Module):
    def __init__(self, mode='batch'):
        super().__init__()
        if mode == 'batch':
            self.linear = torch.nn.Linear(2, 2)
        elif mode == 'channel_last':
            self.linear = torch.nn.Linear(2, 4)

    def forward(self, x1):
        v1 = x1.permute(0, 3, 1, 2)
        v2 = torch.relu(v1)

        if mode == 'batch':
            v3 = v2.view(-1, 2, 4).permute(0, 2, 1)
            v4 = self.linear(v3)
        elif mode == 'channel_last':
            v3 = v2.view(-1, 4, 2).permute(0, 2, 1)
            v4 = self.linear(v3)

        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 4, 2, 3)
