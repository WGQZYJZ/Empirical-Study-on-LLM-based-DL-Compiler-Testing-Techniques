
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        split_sizes = [v1.shape[1], v1.shape[0] // 2]
        return torch.cat([
            torch.split(v1, sizes=sizes, dim=1)[0] for sizes in split_sizes
        ], 1)


# Initializing the model
m = Model()


