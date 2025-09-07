

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x):
        v1  = self.conv(x) 
        v2  = torch.sigmoid(v1) # Add sigmoid function
        v3  = v1 * v2 # Multiplies the result of the conv by the sigmoid output.
        return v3

# Initializing model