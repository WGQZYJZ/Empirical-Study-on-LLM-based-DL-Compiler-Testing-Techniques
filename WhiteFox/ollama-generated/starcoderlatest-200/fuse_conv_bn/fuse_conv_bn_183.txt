
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channels=1, out_channels=3, kernel_size=(4, 4), stride=(2, 2))
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x):
        output = F.conv2d(x, weight=self.conv.weight, bias=self.conv.bias)
        output = F.batch_norm(output, self.bn.running_mean, self.bn.running_var, self.bn.weight,
                              self.bn.bias, True, 0.5)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 1, 16, 8, requires_grad=True)
