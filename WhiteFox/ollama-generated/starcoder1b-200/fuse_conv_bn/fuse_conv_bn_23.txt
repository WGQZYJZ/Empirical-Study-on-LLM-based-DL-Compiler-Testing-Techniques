
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(...)
        self.bn1  = torch.nn.BatchNorm2d(...)

    def forward(self, x1):
        v1 = x1.permute(0, 3, 1, 2)  # X should be 4D (NCHW), where N is the number of batch size
        v2 = self.conv1(v1)          # The main input to the convolution layer
        output = self.bn1(v2)        # The outputs are used as inputs for the next layer, whose output is fed into the final layer
        return output


# Initializing the model
m  = Model()


