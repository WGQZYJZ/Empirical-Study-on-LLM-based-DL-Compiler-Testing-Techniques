
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.conv0 = torch.nn.Conv2d(4, 5, 1)
 
    def forward(self, x1): 
        v1  = self.conv(x1)
        v2  = v1 * 0.7071067811865476
        v3  = torch.erf(v2) + 5
        v4  = v3 - 4 
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 8, 60, 70)


# Initialization for x2_test
x2_test  = torch.randn(5, 3)
x2       = torch.zeros([9 ,5])
x2[:3]   = x2_test


# Initialization for y1_test
y1_test  = torch.randn(7)
y1    = torch.zeros([8 ,3])
y1[0]     = y1_test 

# Initialization for y2_test
y2_test  = torch.randn(4,5)
y2      = torch.zeros([9 ,5])
y2[:4]   = y2_test

x3       = self.conv0(torch.cat((x1[None], x2[None]), dim=1))
x3       = self.conv0(self.conv0(x3))

