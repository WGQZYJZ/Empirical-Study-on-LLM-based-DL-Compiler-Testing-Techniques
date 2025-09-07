
class Model(torch.nn.Module):
    def __init__(self, kernel, stride):
        super().__init__()
        self.conv = torch.nn.Conv2d(kernel, 3, stride) # the batch size is always set to 1 here

        self.bn = torch.nn.BatchNorm2d(num_features=3, num_batches_tracked=1)

    def forward(self, x):
        o1 = self.conv(x).permute(0, 2, 3, 1).contiguous() # Permute the input tensor

        v1 = self.bn(o1)
        v2 = torch.nn.functional.linear(v1, ...)

        return v2


# Initializing the model
m = Model(...)


# Inputs to the model
x = torch.randn(1, 3, 56, 84)
