
class Model(torch.nn.Module):
    def __init__(self, linear):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
        self.linear2 = torch.nn.Linear(2, 5)

    def forward(self, x1):
        t1 = x1[:, :, None]
        v1 = x1.permute(0, 2, 1).contiguous()
        v2 = torch.cat([v1[:, :3, :], v1[:, -4:]], dim=2)
        return self.linear(self.linear2(t2))


# Initializing the model
m = Model(torch.nn.Linear(20, 5).to("cuda"))


