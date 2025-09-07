
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvXd(...) # Conv2d in module API and convXd function in Funtional API

    def forward(self, input_tensor):
        bn  = torch.nn.BatchNormXd(...) # BatchNorm1d in module API and batch_norm function in Functional API
        conv = self.conv1(input_tensor) 
        return bn(conv)

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2, 2) # input tensor with two batch axes and two spatial axes
