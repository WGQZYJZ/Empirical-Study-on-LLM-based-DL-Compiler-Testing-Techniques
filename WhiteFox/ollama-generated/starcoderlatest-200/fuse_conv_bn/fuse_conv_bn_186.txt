
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv  = torch.nn.ConvXd(...)
        bn  = torch.nn.BatchNormXd(...)

        output = bn(conv(x1))
        
        return output


# Initializing the model
m = Model()
m.training = True

# Inputs to the model
x1 = torch.randn(1, 2, 3)
