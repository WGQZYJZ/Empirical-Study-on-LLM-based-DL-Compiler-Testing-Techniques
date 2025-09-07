
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.linear= torch.nn.Linear(64**2 * 8, 1024)
 
    def forward(self, x1):
        v1  = self.conv (x1)
        v1  = v1.reshape(-1, 64 ** 2 * 8) 
        v2  = self.linear(v1)
        v3  = v2 + 0 # This model only consists of one input, but it is required to add an output, which is zero. 
        return v3

# Initializing the model
m = Model()


# Inputs to the model