
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v1, v2  = torch.split(x1, 90, 2) # Split the input tensor into two tensors along dimension 2 with sizes equal to 45 and 45 respectively
        v3  = self.conv(v1 + v2)   # Add both of the split tensors together before feeding it to a convolutional layer.
        return torch.cat([v3, v3], dim=0)

# Initializing the model
m = Model()

