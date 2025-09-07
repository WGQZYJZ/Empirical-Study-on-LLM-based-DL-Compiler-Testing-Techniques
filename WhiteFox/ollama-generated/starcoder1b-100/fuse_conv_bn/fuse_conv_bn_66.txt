
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn   = torch.nn.BatchNorm2d(...)  # X should match with ConvXd

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.nn.functional.batch_norm(v1, ..., False)  # X should be the batch_size_0 and the channel_dim_0 of the input_tensor
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 4, 4, 3)
