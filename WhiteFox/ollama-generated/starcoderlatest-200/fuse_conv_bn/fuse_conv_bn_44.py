
class Model(torch.nn.Module):
    def __init__(self, in_channels):
        super().__init__()

        self.conv1 = torch.nn.Conv2d(in_channels=in_channels, out_channels=64, kernel_size=3, stride=1)
        self.bn1 = torch.nn.BatchNorm2d(num_features=64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)

        self.conv2 = torch.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1)
        self.bn2 = torch.nn.BatchNorm2d(num_features=64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)

    def forward(self, x):
        # ConvXd layer
        v1 = torch.nn.functional.conv2d(x, self.conv1.weight, self.conv1.bias, stride=self.conv1.stride, padding=self.conv1.padding)

        # BatchNormXd layer
        v2 = torch.nn.functional.batch_norm(v1, self.bn1.running_mean, self.bn1.running_var, self.bn1.weight, \
                                self.bn1.bias, training=self.training) 
        
        v3 = torch.nn.functional.conv2d(v2, self.conv2.weight, self.conv2.bias, stride=self.conv2.stride, padding=self.conv2.padding)

        # BatchNormXd layer
        v4 = torch.nn.functional.batch_norm(v3, self.bn2.running_mean, self.bn2.running_var, self.bn2.weight, \
                                self.bn2.bias, training=self.training) 
        
        return v4


# Initializing the model
m = Model(in_channels=1)


