
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1)
 
    def forward(self, x1): 
        v1  = self.conv(x1) # Convolution
        v2  = v1 + torch.ones_like(v1) * 0.75 # Add a constant tensor to the output of the convolution
        v3  = torch.relu(v2)# ReLU activation function

        return v3


# Initializing the model