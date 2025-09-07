
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        return is_valid_splitwithsizes_cat([x1, x2, x3])


