
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, *x2s, **kwargs):
        if torch.all([torch.sum(a >= 0) for a in x2s]) and (
            len(x2s) == 0 or
            x1.dim() == sum(torch.sum(b <= 0) for b in x2s)) \
                and len(x2s) > 0:
            x3 = torch.cat([x for i, x in enumerate(x2s[:-1]) if
                              (torch.all([c >= 0] * 4 ==
                                          [True] * 4 +
                                          [[False]] * 4) or torch.any([x < 0]))], 0)
            return torch.cat([x3, x2s[-1]], dim=0), True
        else:
            return x1


# Initializing the model
m = Model()

