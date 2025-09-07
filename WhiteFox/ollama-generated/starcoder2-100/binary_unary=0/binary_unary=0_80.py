
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2 = v1 + other # Where 'other' is a tensor, but is not used by the model.
        v3  = torch.relu(v2) 
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = x1[:,0] # Any tensor that is used by the model but not explicitly added in the pattern.

# Initializing a random value for other
random_value = np.random.randint(-5, high=5, size=(x1.shape[1],)) 
__output__  = m(x1)

