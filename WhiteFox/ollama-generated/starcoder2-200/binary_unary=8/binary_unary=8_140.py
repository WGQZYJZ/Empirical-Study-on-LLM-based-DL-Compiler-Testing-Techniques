
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other_tensor # Add another tensor to the output of the convolution 
        v4 = torch.relu(v2)
        return v3


# Initializing the model 
m = Model()

# Inputs to the model  
__output__  = m(x1)

