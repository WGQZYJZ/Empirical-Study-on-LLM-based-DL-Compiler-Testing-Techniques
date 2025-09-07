
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.split(x1, split_sizes, dim) 
        v2 = torch.cat([v1[i] for i in range(len(split_sizes))], dim)
        return v6

