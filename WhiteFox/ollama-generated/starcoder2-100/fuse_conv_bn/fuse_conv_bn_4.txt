
class Model(torch.nn.Module):
    def __init__(self, conv=3, batchNorm=2):
        super().__init__()

        self.conv  = torch.nn.ConvXd(in_channels=2, out_channels=10) if conv == 1 else torch.nn.ConvNd(
            in_channels=2, out_channels=10, 
            kernel_size=(3,), groups=4
        )

        self.batchNorm = torch.nn.BatchNormXd(num_features=conv) if batchNorm==1 \
                         or batchNorm == 3 else None 

        self._out_shape = tuple([2] + [2 for _ in range(self.conv.in_channels)] + [10])

    def forward(self, x):
        if self.batchNorm is not None:
            out = torch.nn.functional.convXd(x=x, weight=self.conv.weight) # Passes a convXd layer as input
            out  = out.permute(0, 3, 1, 2) # Reshape the tensor to adapt to batchNorm
            out  = self.batchNorm(out) # Fuse the conv and batchnorm layers 
            out  = out.view(-1)
        else:
            # Model without BN (conv+BN)
            out = torch.nn.functional.convXd(x=x, weight=self.conv.weight).view(-1)
            out = self.conv.bias.expand_as(out)+0*torch.sum(x) # Add bias and sum over channels
        return out, None

# Initializing the model
m  = Model()


# Inputs to the model
inputs = torch.randn(2, 15) + 1
outputs = m(inputs)


# Printing inputs of the model
print("Inputs to the model")
inputs

