
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 6 # Other tensor for the addition operation
        v3 = torch.relu(v2)
        return v3

# Initializing and running a model (please note that `v2` is the input to the `Model` class above.)