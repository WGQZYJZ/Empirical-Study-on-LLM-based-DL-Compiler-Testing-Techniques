
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = conv(x1)
        v2  = v1 * 0.5
        v3  = v1 + other # Subtract 'other' from the output of the linear transformation 
        v4  = torch.nn.functional.relu(v3)  
        return v4

# Initializing the model
m = Model()


# Inputs to the model