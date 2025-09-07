
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 2, kernel_size=3, stride=1)
        self.bn = torch.nn.BatchNorm2d(2)

    def forward(self, x):
        x1 = F.conv2d(x, self.conv.weight, padding=self.conv.padding)
        x2 = F.batch_norm(x, self.bn.running_mean, self.bn.running_var,
                        self.bn.weight, self.bn.bias, training=False)
        return torch.nn.functional.add(x1, x2)


# Initializing the model
m = Model()


