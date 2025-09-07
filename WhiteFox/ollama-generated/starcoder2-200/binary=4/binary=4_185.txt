
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(64 * 64 * 3, 8)
        self.other = torch.randn(1024).to('cuda')
 
    def forward(self, x):
        v1 = linear(x) 
        v2 = v1 + other
        return v2


# Initializing the model
m = Model()

# Inputs to the model
inputs  = torch.randn(64 * 32, 64 * 64).to('cuda')
__output__  = m(input)

# References
1. [Convolution Arithmetic](https://discuss.pytorch.org/t/convolution-arithmetic/59708) - PyTorch Discussions
