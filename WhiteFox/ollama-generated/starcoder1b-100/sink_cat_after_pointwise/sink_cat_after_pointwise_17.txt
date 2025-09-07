
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        # t1 has shape [batch_size, length, channel]
        t1 = x1[:, :, None].repeat(1, 1, x1.shape[2])

        # t2 has shape [batch_size * channels, length]
        t2 = torch.cat([t1, t1], dim=1).view(2, -1)
        t3 = torch.relu(t2)

        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
