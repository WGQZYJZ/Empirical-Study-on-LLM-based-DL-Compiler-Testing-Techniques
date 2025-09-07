
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3,8, 1)
        self.conv2 = torch.nn.Conv2d(3,8, 1)
 
    def forward(self, x):
        
        v1=self.conv1(x)
        v2=v1+self.conv2(x)+other
        v3 =torch.relu(v2)
        return v3

# Initializing the model
model = Model()
__output__  = m(x)

