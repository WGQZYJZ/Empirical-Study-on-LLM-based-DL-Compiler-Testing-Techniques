
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1[:, :, i * 4: (i + 1) * 4] for i in range(2)], dim=1)
        v2 = torch.cat([v1[:, :, :128], v1[:, :, 96:-32]], dim=1)
        return torch.cat([torch.cat([x1[:, :, :64], x1[:, :, 128:]], dim=1),
                        torch.cat([v2[:, :, 0:32], v2[:, :, 32:-16]], dim=1)],
                       dim=1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 4, 5, 7)
