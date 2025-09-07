
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=64, kernel_size=(3, 3), stride=1)
        self.conv2 = torch.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=(3, 3), stride=1)

    def forward(self, x):
        conv1_bn1 = nnf.batch_norm(nnf.conv2d(x, self.conv1)) # fuse batch norm and conv
        conv2_bn2 = nnf.batch_norm(nnf.conv2d(conv1_bn1, self.conv2))
        return nnf.relu(conv2_bn2)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 48, 56)
