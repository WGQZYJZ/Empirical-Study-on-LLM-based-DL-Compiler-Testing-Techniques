
class Model(torch.nn.Module):
    def __init__(self, shape=(128,), in_channels=3, out_channels=45):
        super().__init__()

        # Convolution 1
        self.conv1 = torch.nn.ConvNd(shape) 
        self.conv1.in_channels = in_channels 
        self.conv1.out_channels = in_channels
        
        # Batch normalization 1
        self.bn1 = torch.nn.BatchNormNd(
            shape, affine=True, track_running_stats=True,
            weight=torch.nn.Parameter(
                torch.ones([in_channels], requires_grad=False)))
        self.bn1.running_mean.requires_grad_(True)
        self.bn1.running_var.requires_grad_(True)

        # Convolution 2 (conv 3D, bn 4D)
        self.conv2 = torch.nn.ConvNd(shape)
        self.conv2.in_channels = in_channels 
        self.conv2.out_channels = out_channels
        
        # Batch normalization 2
        self.bn2 = torch.nn.BatchNormNd(
            shape, affine=True, track_running_stats=False, 
            weight=torch.nn.Parameter(
                torch.ones([in_channels], requires_grad=False)))
        self.bn2.running_mean.requires_grad_(False)

        # Weights to 0 after conv1
        self._set_zero_weights(self.conv1)

    def forward(self, x):
        v1 = self.conv1(x) 
        v1 = self.bn1(v1) 
        return self.conv2(v1), v1

    @torch._overload_impl
    # Input shape: [N, Cin] where Cin=in_channels
    def _set_zero_weights(self):
        # Input shape: [N, 3, Cin] where Cin=in_channels
        def _set_zero_weights_(self, input):
            self.weight = torch.nn.Parameter(
                torch.zeros([input], requires_grad=False))

        # Return the implementation 
        return _set_zero_weights_

    @torch._overload
    def _set_zero_weights(self, *args, **kwargs):
        pass


# Initializing the model 
m = Model()
