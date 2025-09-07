
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 4)

    def forward(self, x1):

        # Create a variable to store the output of convolution + batch norm
        conv_out = None
        # Get the current running mean for BatchNorm
        bn_mean = torch.zeros(x1.size()[0])
        with torch.no_grad():
            for batch in range(x1.shape[0]):
                # Create a 5-D Tensor for convolution operation
                conv_in = x1[batch].expand(-1, -1, 5)

                # Fuse Conv+Bn operation into a single Conv operation
                conv_out = torch.nn.functional.conv2d(conv_in, conv.weight, conv.bias, conv.stride)
                conv_out += bn(conv_out)
                batchnorm_output[batch] = bn_mean[batch]

        return conv_out

# Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(2, 5, 3, 4)
 
__output__  = m(x1)