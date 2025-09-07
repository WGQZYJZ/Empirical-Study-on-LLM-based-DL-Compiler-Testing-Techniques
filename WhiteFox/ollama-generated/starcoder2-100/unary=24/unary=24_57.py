
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.leakyrelu  = torch.nn.LeakyReLU()
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = self.leakyrelu(v1) 
        return v2

# Initializing the model
m = Model()

 # Inputs to the model