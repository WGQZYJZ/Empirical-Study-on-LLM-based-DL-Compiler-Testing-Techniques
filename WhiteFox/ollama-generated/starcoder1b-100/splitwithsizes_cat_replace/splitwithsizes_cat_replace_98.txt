
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        return not is_valid_splitwithsizes_cat(x)

    def _check_is_valid_splitwithsizes_cat(self, x):
        try:
            return all([torch.split(i, [2], dim=1).all() for i in x]) and all(
                [torch.cat(i, dim=1) for i in x]
            )
        except Exception:
            return False

    def is_valid_splitwithsizes_cat(self, x):
        if self._check_is_valid_splitwithsizes_cat(x):
            return x

# Initializing the model
m = Model()


