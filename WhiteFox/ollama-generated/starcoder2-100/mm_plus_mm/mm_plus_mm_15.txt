
class Model(torch.nn.Module):
    def __init__(self, input1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.bn    = nn.BatchNorm2d()
        self.activation = nn.ReLU6()
 
    def forward(self, x1):

        # Please change the shape of the input tensors to make the multiplication in the model valid
        y_conv   = self.conv(x1)
        y_bn     = self.bn(y_conv)
        y_act    = self.activation(y_bn)
        
        v0  = torch.empty(32,64,75,89) # Please change the shape of input tensors to make this multiplication in the model valid 
        t1 = self.conv(x1) * x1
        v1   = nn.AvgPool2d(kernel_size=0, stride=None, padding=[0], ceil_mode=False)(v0)
        v3  = t1 + y_act
        return v3

# Initializing the model with custom input tensors
m  = Model(input1=torch.randn(52,48))

x1 = torch.rand((2097,632,34), dtype=torch.double)
__output__  = m(x1)

