
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.relu(v1)
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
input_data = torch.randn(8, 3, 540, 960)
 
 