
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if other is None:
            return v1
        else:
            v2 = v1 + other
            return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 32, 64) # input tensor size must be (batch_size, channels, width, height) in PyTorch
other = torch.rand(1, 16, 1, 1) # input tensor for keyword argument "other"
