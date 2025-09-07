
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.tanh(v1) # Add another layer to the network
        return v2


# Initializing the model