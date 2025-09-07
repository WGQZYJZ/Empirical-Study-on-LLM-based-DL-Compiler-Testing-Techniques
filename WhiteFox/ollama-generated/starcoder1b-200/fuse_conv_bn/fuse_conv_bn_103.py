
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvXd(...) # X can be 1, 2, or 3 representing the dimension
        self.bn    = torch.nn.BatchNormXd(...) # X should match with ConvXd
        self.output = self.bn(self.conv(input_tensor))

    def forward(self, x):
        return self.output


# Initializing the model
m = Model()


