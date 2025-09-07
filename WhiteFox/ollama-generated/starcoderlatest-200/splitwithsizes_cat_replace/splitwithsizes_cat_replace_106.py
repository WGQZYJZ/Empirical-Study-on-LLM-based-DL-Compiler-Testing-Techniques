
class Model(torch.nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.conv = torch.nn.Conv2d(input_dim, 32, 3, stride=1, padding=1)

    def forward(self, x1):
        t0 = self.conv(x1)
        split_tensors = torch.split(t0, split_sizes, dim)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim)
        return True


# Initialization
m = Model()


# Inputs to the model
x1 = torch.randn(32, 64, 28, 28)
