
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(in_features=8, out_features=1)
 
    def forward(self, x):
        # Apply pointwise convolution to the input tensor
        v = self.conv(x)
 
        # Create a boolean tensor where each element is True if the corresponding element in v is greater than 0, and False otherwise
        t = torch.where(v > 0, v, 1 - v)
 
        # Multiply the output of the linear transformation by the negative slope
        s = t * -1e6
 
        # If the corresponding element in s is greater than zero, return the corresponding element from v, otherwise return one minus the corresponding element from v.
        r = torch.where(t > 0, v, 1 - v)
        return s + r


# Initializing the model
m = Model()


