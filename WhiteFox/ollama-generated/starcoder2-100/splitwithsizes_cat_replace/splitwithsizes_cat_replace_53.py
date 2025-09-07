
class Model(torch.nn.Module):
    def __init__(self, num_split=2, inputsize=(3, 64, 1078)):
        super().__init__()
        self.conv = torch.nn.Conv2d(inputsize[0], 8, 1, stride=1, padding=1)
 
    def forward(self, x): 
        v1 = self.conv(x)
        return torch.split(v1, split_sizes=[256] * num_split, dim=-3)[-1]
# Initializing the model with split = 4
m = Model(num_split=4)

# Inputs to the model
x = torch.randn((4096 + (4 - 1)*256), 8, 64, 3) # This will be an array of 75 arrays each of size 3 x 64 x 64 with total size of 34816.
split_sizes = [v * v for v in range(m.conv._split_sizes)]

