
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=4)

        self.conv2 = torch.nn.Conv2d(8, 6, kernel_size=5)

    def forward(self, x):
        t1 = self.conv1(x).clone()
        t2 = self.conv2(t1)
        t3 = torch.relu(t2)
        return t3

# Initializing the model
m  = Model()
 
# Inputs to the model
x = torch.randn(1, 3, 840, 960)
__output__  = m(x).clone().detach()

