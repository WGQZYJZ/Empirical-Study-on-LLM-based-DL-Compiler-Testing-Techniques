
class Model(torch.nn.Module):
    def __init__(self, x1):
        super().__init__()
        conv = torch.nn.Conv2d(...)  # X can be 1, 2 or 3 representing the dimension
        bn   = torch.nn.BatchNorm2d(...)  # X should match with Conv2d

        self.conv1 = conv(x1)
        self.bn    = bn(self.conv1)

    def forward(self):
        v1 = self.conv1.permute(0, 2, 3, 1)
        v2 = torch.nn.functional.batch_norm(v1, self.bn.weight, self.bn.bias, self.bn.running_mean,
                                            self.bn.running_var, self.bn.num_batches_tracked)
        return v2


# Initializing the model
m = Model(x1)


