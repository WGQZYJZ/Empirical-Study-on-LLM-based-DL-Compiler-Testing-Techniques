
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.125):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        # We want to create a mask where each element in v1 is greater than the negative slope. Therefore we use the > operator for this purpose. 
        # We can also use < and <= operators for this. The difference is that in PyTorch, 0 is considered greater than any other number, whereas in Python, 0 is always greater than anything else
        v2 = v1 > self.negative_slope
        # Apply LeakyReLU on v2 to create a tensor with the same shape as v1 where each element is set to either v1 or negative_slope
        v3 = torch.where(v2, v1, -self.negative_slope)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
