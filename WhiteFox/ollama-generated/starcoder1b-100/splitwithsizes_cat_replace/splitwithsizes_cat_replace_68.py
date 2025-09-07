
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes  = [2, 2, 4]
        concatenated_tensor = torch.cat([torch.split(x1, split_sizes[i], dim=0)[i] for i in range(len(split_sizes))], dim=0)
        v = self.conv(concatenated_tensor)
        return v


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(4, 3, 64, 64)
