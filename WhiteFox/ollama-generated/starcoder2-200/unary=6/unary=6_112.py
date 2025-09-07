
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 + 3
        v3  = F.relu6(v2) # ReLU6 activation function
        v4  = v3 * 6 / 7
        return v4
 
# Initializing the model with some weights for initialization
m = Model()


# Inputs to the model. Make sure that these inputs are not always the same!
x1 = torch.randn(2, 3, 60, 50) 

