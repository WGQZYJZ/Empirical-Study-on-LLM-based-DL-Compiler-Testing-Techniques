
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)

        split_sizes = [2]
        concatenated_tensor = torch.cat([torch.split(v1, split_sizes, dim=0)[i] for i in range(len(split_sizes))], dim=0)
        return concatenated_tensor

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
v2 = m(x1)  # v2 is a concatenated tensor of shape [1, 8, 15, 15], all tensors are split along dimension 0

