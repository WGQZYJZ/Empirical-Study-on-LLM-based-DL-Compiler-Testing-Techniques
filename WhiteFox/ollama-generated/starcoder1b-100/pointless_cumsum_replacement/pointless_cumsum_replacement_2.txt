
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.full([x.shape[0], 32], 1., device=device)


