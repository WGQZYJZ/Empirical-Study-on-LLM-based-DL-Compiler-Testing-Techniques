 
class Model(torch.nn.Module):
    def __init__(self, channels=1):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)

    def forward(self, input_tensor):
        bn = torch.nn.BatchNormXd(...)
        output = bn(self.conv(input_tensor))
        return output

# Initializing the model 
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
