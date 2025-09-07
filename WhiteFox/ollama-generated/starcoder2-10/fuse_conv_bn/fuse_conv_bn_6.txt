
class Model(torch.nn.Module):
    def __init__(self, inputSize=28*28):
        super().__init__()

        self.conv1 = torch.nn.Conv2d(
            in_channels=inputSize//4, 
            out_channels=30, 
            kernel_size=5)

    def forward(self, x):

        self.batchnorm  = torch.nn.BatchNorm2d(num_features=30, momentum=0.1, affine=True)
        v1  = self.conv1(x).permute([0, 1, 4, 5])
        return v1


# Initializing the model
model  = Model()


# Inputs to the model
x  = torch.randn(32,  784)
__output__  = model(x)