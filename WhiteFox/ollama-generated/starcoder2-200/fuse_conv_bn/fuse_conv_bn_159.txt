
class Model(torch.nn.Module):
    def __init__(self, convXd, batchNormXd):
        super().__init__()

        self.conv1 = torch.nn.ConvXd(40, 32, 7)
        self.batchnorm1 = torch.nn.BatchNormXd(32)

    def forward(self, x1):
        conv_output = self.convXd(x1) # ConvXd is an alias to torch.nn.functional.convXd()

        return self.batchNormXd(convOutput)


# Initializing the model
m  = Model()

# Inputs for the model (use a non-empty tensor as input). The input shape should be 1 X 40 X 32 X 7, which matches the number of channels and kernel size. 
x1  = torch.randn(1, 40, 32, 7)

 __output__  = m(x1)
