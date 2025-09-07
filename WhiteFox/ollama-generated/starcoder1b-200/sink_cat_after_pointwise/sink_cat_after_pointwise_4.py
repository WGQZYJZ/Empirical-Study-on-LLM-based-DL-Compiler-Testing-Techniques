
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        # Some initialization logic
        v1 = torch.cat([x1[:, :, None], x1[:, :, :, None]], dim=2)
        v2 = x1.view(-1, 10)
        return torch.relu(v3)


# Initializing the model
m = Model()


