
class Model(torch.nn.Module):
    def __init__(self, conv_channel, num_classes):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channels=1, out_channels=conv_channel, kernel_size=(3, 3), padding=(1, 1)) 
        self.bn = torch.nn.BatchNorm2d(num_features=self.conv._get_linearized_dim(), affine=True)
        self.fc = torch.nn.Linear(in_features=self.conv._get_linearized_dim(), out_features=num_classes)
       
    def forward(self, x1): 
        conv  = self.conv(x1)
        bn    = self.bn(conv)
        output   = bn # Here, we fuse the convolution and batch normalization layers into a single layer
        
        # A functional equivalent of the above code
        # conv = torch.nn.functional.conv2d(input_tensor=x1, weight=self.conv.weight, bias=self.conv.bias) 
        # bn   = self.bn(conv) # We still fuse the convolution and batch normalization layers into a single layer
        return self.fc(output)

# Initializing the model 
m = Model()

# Inputs to the model 
x1 = torch.randn(5, 1, 32, 32) 
 