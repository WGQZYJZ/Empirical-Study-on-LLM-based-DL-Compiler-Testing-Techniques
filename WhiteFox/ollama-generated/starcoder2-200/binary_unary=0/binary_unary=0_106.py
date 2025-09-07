
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v4  = v1 + other_tensor
        v5  = torch.relu(v4) # Note: the model does not contain the ReLU layer
        return v2

# Initializing the model