
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 5)
        self.conv2 = torch.nn.Conv2d(64, 128, 5)
        self.conv3 = torch.nn.Conv2d(128, 64, 5)
 
    def forward(self, x):
        t1  = self.conv1(x)
        t2  = t1  * 0.5
        t3  = t1  * 0.7071067811865476
        t4  = torch.erf(t3)
        t5  = t4  + 1
        t6  = t2  * t5
        t7  = t6  * 0.7978845608028654
        t8  = torch.tanh(t7)
        t9  = t8  + 1
        t10 = t1  * t9
 
        return t10


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
