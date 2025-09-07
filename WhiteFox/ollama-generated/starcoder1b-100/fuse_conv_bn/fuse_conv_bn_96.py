
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn    = torch.nn.BatchNormXd(...)  # X should match with ConvXd

    @torch.jit._script_method
    def forward(self, input_tensor):
        conv = self.conv(input_tensor)
        bn   = self.bn(conv)
        return bn

# Inputs to the model
x1 = torch.randn(1, 2, 2)
