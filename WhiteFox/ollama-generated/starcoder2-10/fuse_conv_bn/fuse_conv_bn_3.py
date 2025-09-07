
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): 
        conv  = torch.nn.Conv2d(in_channels=3, out_channels=40, kernel_size=(7, 7)) # Convolution layer
        bn    = torch.nn.BatchNorm2d(num_features=40)                             # Batch normalization layer with 40 features
        v1    = conv(x1)                                                           # Forward pass 
        v2    = bn(v1)                                                             # Use the same tensor as input of BatchNorm layer (after conv) to initialize batchnorm running stats.
        v3    = torch.nn.functional.conv2d(input=v2,             # Fuse conv and BN in eval mode
                                          weight=conv.weight, 
                                          bias   =bn.bias    )  
        return bn(v3)                                                            # Return the output of BatchNorm layer without performing fusing


# Initializing the model