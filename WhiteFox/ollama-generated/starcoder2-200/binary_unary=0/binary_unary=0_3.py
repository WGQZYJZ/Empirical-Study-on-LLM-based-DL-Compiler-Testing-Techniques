
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.conv01  = torch.nn.Conv2d(3, 4, 1)

    def forward(self, x1, x2): 
        v1  = self.conv(x1)
        v2  = self.conv01(v1)
        v3  = v1 + other # ADD
        v4  = torch.relu(v3)

        return v4

# Initializing the model
m  = Model()

# Inputs to the model (for example, both of them are not None)
x2  = torch.randn(1, 3, 60, 89)
x1 = torch.randn(1, 3, 57, 45)

 __output__  = m(x1, x2)
 
 
