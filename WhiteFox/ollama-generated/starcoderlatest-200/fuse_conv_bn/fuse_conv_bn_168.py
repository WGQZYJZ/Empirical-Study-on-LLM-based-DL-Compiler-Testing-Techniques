
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 1, kernel_size=(3,3), stride=2) # conv layer with a filter of size (3,3). The input is the original tensor and the output is a filtered tensor with a padding of [1] * len(kernel_size)/2
        self.bn = torch.nn.BatchNorm2d(1) # batch norm layer

    def forward(self, x):
        conv_output  = self.conv1(x) # input: original image; output: filtered tensor with a padding of [1] * len(kernel_size)/2
        conv_output = self.bn(conv_output) # input: filtered tensor with a padding of [1] * len(kernel_size)/2; output: filtered tensor after batch norm

        return conv_output

# Initializing the model
m = Model()

 # Inputs to the model
x = torch.randn(1, 3, 100, 100)
