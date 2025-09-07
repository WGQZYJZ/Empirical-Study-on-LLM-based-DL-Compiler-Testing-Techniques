
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        split_sizes = [4] + [2] * len(v1.shape[0:-2])
        concatenated_tensor = torch.cat([torch.split(v1, split_sizes, dim=1)[i] for i in range(len(split_sizes))], dim=1)
        return concatenated_tensor


# Initializing the model
m = Model()
