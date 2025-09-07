
class FuseConvBN(torch.nn.Module):
    def __init__(self,  input_channel, output_channel):
        super().__init__()

        self.conv1 = torch.nn.Conv2d(input_channel, output_channel, kernel_size=3)
        self.bn1   = torch.nn.BatchNorm2d(output_channel)

    def forward(self, x): 
        out  = torch.nn.functional.conv2d(x,
                                          weight    = self.conv1.weight,
                                          bias      = self.conv1.bias,
                                          stride    = self.conv1.stride,
                                          padding   = self.conv1.padding,
                                          dilation  = self.conv1.dilation)
        out = torch.nn.functional.batch_norm(out, self.bn1.running_mean, self.bn1.running_var,
                                             self.bn1.weight, self.bn1.bias, self.bn1.momentum, 
                                             0.5, eps=self.bn1.eps)
        return out

# Initializing the model
m = FuseConvBN(input_channel=2, output_channel=3)

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 80)
