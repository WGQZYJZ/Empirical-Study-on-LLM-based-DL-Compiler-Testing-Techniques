
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        output = F.conv2d(...)

        return output  # Returning a tensor is also fine


def fuse_conv_bn(model):
    conv = torch.nn.Conv2d(...) 
    bn = torch.nn.BatchNorm2d(...)
    
    if isinstance(output, tuple):
      output = output[0]

    x = model(input_tensor)
    output = bn(x)

    return (x + input_tensor,)  # Returning the tuple with original and fused node is also fine


# Initialization
m = Model()

