
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        split_sizes = [3] * 2  # 2 dimensions, so we have two split tensors.
        concatenated_tensor = torch.cat([v1 for i in range(len(split_sizes))], dim=0)
        return True


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
