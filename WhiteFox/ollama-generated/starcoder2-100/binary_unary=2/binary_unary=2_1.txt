
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1): 
        v1  = self.conv(x1)
        v2  = v1 - other  # subtract a tensor from the output of convolution
        v4  = F.relu(v2)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) 
