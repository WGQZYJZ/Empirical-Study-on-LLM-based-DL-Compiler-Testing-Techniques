
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1  = torch.nn.ConvXd(...) # X can be 1, 2, or 3 representing the dimension
        self.bn1    = torch.nn.BatchNormXd(...) # X should match with ConvXd
        self.conv2  = torch.nn.ConvXd(...) # X can be 1, 2, or 3 representing the dimension
        self.bn2    = torch.nn.BatchNormXd(...) # X should match with ConvXd

    def forward(self, x1):
        conv = torch.nn.functional.convXd(x1, self.conv1.weight)  # X is the input tensor of the convolution layer
        bn   = torch.nn.functional.batch_norm(conv, training=False)
        output  = self.bn2(bn)
        return output


# Inputs to the model
x1 = torch.randn(1, 2, 2)
