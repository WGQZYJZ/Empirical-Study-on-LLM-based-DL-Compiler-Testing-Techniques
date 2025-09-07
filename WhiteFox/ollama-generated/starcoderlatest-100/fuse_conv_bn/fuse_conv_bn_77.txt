 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 2, kernel_size=2, stride=1)

    def forward(self, x):
        conv_out = self.conv(x)
        bn_out = F.batch_norm(conv_out, gamma=None, beta=None, training=False)
        return bn_out


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 1, 3, 2)
