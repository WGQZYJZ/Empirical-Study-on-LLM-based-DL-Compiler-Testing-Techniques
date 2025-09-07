
class Model(torch.nn.Module):
    def __init__(self, conv=4):
        super().__init__()

        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=(7,5))
        
        self.bn1   = torch.nn.BatchNormNd(conv) # N should match with ConvXd
        self.conv2 = torch.nn.Conv2d(8, 16, (4, 3), padding=0)
        
    def forward(self, x):
        v1  = x.permute((1, 0))
        v2  = self.bn1(v1, track_running_stats=True)
        
        v3  = torch.nn.functional.conv2d(v1, self.conv1.weight, bias=None, stride=(4, 5), padding=(7-4)//2, dilation=1, groups=1)

        v4  = torch.nn.functional.batch_norm(v3, self.bn1.running_mean[0], self.bn1.running_var[0], self.bn1.weight[0], \
                                              self.bn1.bias[0], momentum=self.bn1.momentum)

        v5  = torch.nn.functional.conv2d(v4, self.conv2.weight, bias=None, stride=(3,4), padding=(0,), dilation=1, groups=1)
        return v5


# Initializing the model
m  = Model()

# Inputs to the model
x = torch.randn(3, 7, 8)
