
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvXd(...) # X can be 1, 2, or 3 representing the dimension
        self.bn    = torch.nn.BatchNormXd(...) # X should match with ConvXd

    @torch.jit._trace_module()
    def forward(self, x):
        v = x.permute(0, 2, 1)

        # The convolution layer and batch normalization layer are fused into a single operation
        conv_output = self.conv(v) # Output of the convolution is used as the input to the batch norm layer 
        bn_output   = self.bn(conv_output) # Output of the batch norm layer is removed

        return bn_output


# Initializing the model
m = Model()


