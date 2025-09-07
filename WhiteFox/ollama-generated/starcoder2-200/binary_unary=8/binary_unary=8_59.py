
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other_tensor # Another tensor is added to the output of conv (v1). 
        v3 = torch.relu(v2)  # ReLU function is applied to the output of the addition operation.
        return v3

# Initializing the model:  
m = Model()

