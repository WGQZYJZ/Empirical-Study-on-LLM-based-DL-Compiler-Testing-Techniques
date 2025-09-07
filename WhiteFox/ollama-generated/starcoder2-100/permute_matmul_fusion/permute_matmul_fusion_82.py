
class Model(torch.nn.Module):
    def __init__(self, t1=None):
        super().__init__()
        self.t1 = t1 if t1 is not None else torch.randn((2, 3))
        self.linearA = torch.nn.Linear(50, 1)

    def forward(self, t2):
        v1 = torch.bmm(self.t1[:, :, 0:2].permute(0, 2, 1), t2).sum(dim=1) + self.linearA(self.t1[:2]).squeeze()
        return v1

# Initializing the model