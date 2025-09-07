
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, (3, 3), (1, 1))
        self.batch_norm = torch.nn.BatchNorm2d(64)

    def forward(self, x1):
        y = x1[0]
        # Do not fuse conv and batch norm layers if the batch norm layer is in evaluation mode
        if not self.training:
            y = self.batch_norm(y)
            return F.avg_pool2d(y, (4, 4), stride=(2, 2))
        else:
            return F.conv2d(y, self.conv1.weight, self.conv1.bias, padding=self.conv1.padding,
                              stride=self.conv1.stride)

# Initializing the model
m = Model()

