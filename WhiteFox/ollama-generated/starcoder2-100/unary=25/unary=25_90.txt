
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv(x)
        v2  = torch.relu(v3) # replace torch.relu with torch.leaky_relu
        return v4


# Initializing the model