
class Model(torch.nn.Module):
    def __init__(self, conv_layer: torch.nn.Conv2d, batch_norm_layer: torch.nn.BatchNorm2d):
        super().__init__()
        self.conv = conv_layer
        self.bn = batch_norm_layer

    def forward(self, input_tensor: torch.Tensor):
        conv  = F.conv2d(...) # Fuse the conv layer and bn layers to a single one.
        bn    = F.batch_norm(...) 
        output= bn(conv(input_tensor))
        return output


# Initializing the model
m = Model(..., ... )


