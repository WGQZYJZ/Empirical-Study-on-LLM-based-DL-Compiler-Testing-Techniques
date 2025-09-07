
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(3, 64, 1)
        self.conv3 = torch.nn.Conv2d(57903360, 1, 1)
        self.conv4 = torch.nn.Conv2d(8, 64, 1)
 
    def forward(self, x):
        t1  = x * 0.5 + -2.5
        t2  = self.conv3(t1) / self.conv4(t2)
        return t2


# Initializing the model:
m = Model()
 

__output__  = m(torch.randn(8, 9, 7))


