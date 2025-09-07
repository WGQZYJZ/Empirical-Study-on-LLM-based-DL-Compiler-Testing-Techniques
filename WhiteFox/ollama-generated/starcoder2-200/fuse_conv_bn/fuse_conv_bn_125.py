
class Model(torch.nn.Module):
    def __init__(self, conv_kernel_size = 3):
        super().__init__()
        self.conv1  = torch.nn.Conv2d(in_channels=3, out_channels=8, kernel_size=[conv_kernel_size, conv_kernel_size])
        self.conv2  = torch.nn.Conv2d(in_channels=8, out_channels=40, kernel_size=[1, 1], padding=[0, 0], stride=[1, 1])
        self.bn1  = torch.nn.BatchNorm2d(num_features=8)

    def forward(self, x):
        conv1 = self.conv1(x)
        conv2 = self.conv2(conv1)

        # Apply batch normalization to the output of the convolution layer and remove the bias parameter from the conv2 module 
        bn1  = torch.nn.functional.batch_norm(conv2, weight=None, bias=None, running_mean=None, 
                                      running_var=None, training=True)
        return bn1

# Initializing model
m  = Model()
m._enable_fuse_add_relu_() # enable fused_bn_add_relu
__output__  = m(x).flatten().mean(-1).round()

