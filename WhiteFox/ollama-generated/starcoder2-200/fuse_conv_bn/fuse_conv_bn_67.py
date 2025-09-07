
class Model(torch.nn.Module):
    def __init__(self, conv=1):
        super().__init__()
        self.conv  = torch.nn.ConvXd(32, 64, 5) if conv else torch.nn.Conv2d(32, 64, 5)
        self.bn   = torch.nn.BatchNormXd(64)

    def forward(self, x):
        y1  = self.conv(x)
        y2  = self.bn(y1)

        return y2

m  = Model()

 # Input to the model
 x  = torch.rand(8, 32, 450, 600).requires_grad_()

 # Executing the model in training mode and using the default convolution layer
 __output1__  = m(x)

 # Executing the model in training mode and using the Conv2d layer for the first operation. The batch normalization layer is still present in this case.
 m.conv  = torch.nn.Conv2d(*m.conv.weight.size(), *m.conv.bias.size())
 __output2__  = m(x)

 # Executing the model in evaluation mode and using the default convolution layer. The batch normalization layer is still present in this case.
 m.train()
  __output3__  = m(x)
  
 # Executing the model in evaluation mode after the ConvXd->Conv2d Xform optimization, 
 # where `fuse_conv_bn` is triggered and fuses the convolution and batch normalization layers.
 # The resulting convXd operation will be replaced with a single Conv2d operation. 
  __output4__  = m(x)
  
