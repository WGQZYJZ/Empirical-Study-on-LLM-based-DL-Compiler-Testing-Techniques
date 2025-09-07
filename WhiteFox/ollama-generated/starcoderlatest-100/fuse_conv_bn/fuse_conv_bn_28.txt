
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        # Fusing a batch norm layer with convolution layer: (x1 - running_mean) * gamma + beta
        v = torch.nn.functional.conv2d(x1, self.conv.weight, self.conv.bias, self.conv.stride)
        output = torch.nn.functional.batch_norm(v - self.conv.running_mean, self.conv.running_var, 
                                             weight=self.conv.weight, bias=self.conv.bias)

        return output
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 16, 32, 32)
