
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.split = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.cat   = torch.nn.Conv2d(dim + 3 * (len(split_sizes) - 1), 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        t1  = torch.split(x, split_sizes, dim)
        t2  = [self.split(v) for v in t1]
        return self.cat(torch.cat([*t2], dim))

