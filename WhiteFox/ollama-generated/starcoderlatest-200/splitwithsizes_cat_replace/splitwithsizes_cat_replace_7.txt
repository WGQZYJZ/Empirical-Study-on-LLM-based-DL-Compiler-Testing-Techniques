
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = split_tensors = torch.split(x1, [5], dim)
        v2 = cat_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim)
        return v6

