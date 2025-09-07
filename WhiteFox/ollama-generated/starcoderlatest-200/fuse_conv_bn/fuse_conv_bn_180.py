
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 6, 3)

    def forward(self, x1):
        conv_output = self.conv1(x1)
        batchnorm_output = F.batch_norm(conv_output, (0))

        return batchnorm_output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 16, 16)
