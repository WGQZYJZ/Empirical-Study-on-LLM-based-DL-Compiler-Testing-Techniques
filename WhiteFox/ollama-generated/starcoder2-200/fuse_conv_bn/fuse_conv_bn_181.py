
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv  = torch.nn.Conv2d(in_channels=x1.size(-3), out_channels=8, kernel_size=(5,), stride=(2,))
        bn    = torch.nn.BatchNorm2d(num_features=conv.out_channels)
        output   = bn(conv(x1))
        return 1

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(4,3,8,9)
