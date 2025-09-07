
class Model(torch.nn.Module):
    def __init__(self, kernelsize=3):
        super().__init__()

        self.conv = torch.nn.Conv2d(in_channels=10, out_channels=10,
                                    kernel_size=kernelsize)
        self.bn = torch.nn.BatchNorm2d(num_features=10)

    def forward(self, x): 
        output = self.conv(x).permute([0] + list(range(2, len(output.shape))) + [1]) # permute input shape (N, 10, C, H, W) to (N, C, H, W, 10)
        output = torch.nn.functional.batch_norm(
            output, momentum=0., eps=self.bn.eps, 
            weight=self.bn.weight, bias=self.bn.bias) # bn module is not in evaluation mode by default

        return output

# Initializing the model
m  = Model()

