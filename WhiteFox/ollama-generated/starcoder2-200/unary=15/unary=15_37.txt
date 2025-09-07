
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v3  = self.conv(x2) # Convolution 
        v4  = torch.relu(v3) # ReLU activation function 
        return v4


# Initializing the model