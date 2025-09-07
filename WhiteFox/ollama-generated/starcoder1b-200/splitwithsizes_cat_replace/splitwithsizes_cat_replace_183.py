
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def is_valid_splitwithsizes_cat(self, x1, s1, s2):
        