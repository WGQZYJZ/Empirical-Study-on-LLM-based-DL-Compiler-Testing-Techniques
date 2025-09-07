
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv  = torch.nn.ConvXd(x1) # X should be 1 or 2 
        conv_bn  = torch.nn.BatchNormXd(conv)
        return torch.nn.functional.batchnorm(conv_bn(x))

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(3, 4, 5)
x2  = torch.randn(7, 6, 8)
__output1__ = m(x1) # Fused conv/bn is created and it is used directly by other nodes in the graph.

