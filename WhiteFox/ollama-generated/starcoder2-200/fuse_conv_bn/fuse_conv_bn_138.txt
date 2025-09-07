
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.Conv2d(in_channels=3, out_channels=64, kernel_size=(7, 7), stride=(2, 2),
                               padding=(3, 3))

        bn = torch.nn.BatchNorm2d(num_features=conv._packed_params['weight'].size(-1))
        output = bn(conv(x1))

        return output

# Initializing the model
m  = Model()

# Inputs to the model