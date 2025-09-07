
class Model(torch.nn.Module):
    def __init__(self, input_size=10):
        super().__init__()

        self.conv = torch.nn.Conv2d(input_size, 3, kernel_size=(5, 5), stride=(2, 2))
        self.conv.weight.requires_grad_(False)
        self.bn = torch.nn.BatchNormNd(num_features=100).eval()

        self._init_weights()

    def forward(self):
        return self.conv(input_tensor).permute(0, 2, 1)

    def _init_weights(self):
        self.conv = torch.nn.ConvNd(
            [10], 
            kernel_size=[5, 5], 
            stride=(2, 2), 
            bias=True
        )


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 10) # a 3-by-10 input tensor for the model

# Fusion result from the optimizer.
m(x1).permute(0, 2, 1)

