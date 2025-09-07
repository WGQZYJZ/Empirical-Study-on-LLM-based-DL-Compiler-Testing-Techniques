
class ConvBnModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

        # Convolution, 3d.
        self.conv = torch.nn.Conv3d(128, 50, kernel_size=1)

        # Batch normalization, 3d.
        self.bn   = torch.nn.BatchNorm3d(50)

    def forward(self):
        conv     = self.conv
        bn       = self.bn

        # Use the model to create a input tensor for Conv3d and BN3d.
        v1          = torch.rand(2, 128, 40, 96)

        # Apply batch norm and then convolution.
        v_output    = torch.nn.functional.batch_norm(v1, running_mean=None, running_var=None, weight=bn.weight, bias=bn.bias, eps=bn.eps, momentum=0.95)
        conv_output = torch.nn.functional.conv3d(v_output, conv.weight, bias=conv.bias, stride=(2,), padding=(1,))

        # Fuse BN and Conv3d.
        v_output = torch.nn.functional.batch_norm(conv_output)

        return v_output

# Initializing the model
model  = ConvBnModel()

