

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self,x1): 
        v0  = self.conv(x1)
        v1  = v0 - other # Subtraction
        v4  = torch.relu(v1)  # ReLU
        return v4
 

# Initializing the model
m = Model()


# Inputs to the model