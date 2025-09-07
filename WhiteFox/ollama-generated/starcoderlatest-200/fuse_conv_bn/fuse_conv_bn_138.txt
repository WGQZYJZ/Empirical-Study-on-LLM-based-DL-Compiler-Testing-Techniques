
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(2, 10, kernel_size=3)

    def forward(self, x1):
        conv = self.conv(x1) # ConvXD will be optimized if the input shape is compatible with the kernel_shape parameter in __init__ method
        bn = torch.nn.functional.batch_norm(conv) # BatchNormXd will be optimized in evaluation mode
        return bn

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 300, 400)
