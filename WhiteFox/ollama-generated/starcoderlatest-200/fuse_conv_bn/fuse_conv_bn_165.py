
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 2, kernel_size=3)
        self.bn = torch.nn.BatchNorm2d(2)

    def forward(self, x1):
        conv_output = F.conv2d(x1, self.conv1.weight, bias=self.conv1.bias) # ConvXd functional API equivalent is used here. 
        output  = F.batch_norm(conv_output, self.bn.running_mean, self.bn.running_var, self.bn.num_batches_tracked, momentum=0.5, eps=1e-04) # BatchNormXd functional API equivalent is used here. 
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 1, 28, 28)
