
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.ConvXd(...)
        bn = torch.nn.BatchNormXd(...)
        output = bn(conv(input_tensor))
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
