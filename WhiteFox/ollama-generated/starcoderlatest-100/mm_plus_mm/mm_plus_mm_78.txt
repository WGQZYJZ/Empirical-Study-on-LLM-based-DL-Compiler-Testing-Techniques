
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=1, stride=1)
        self.conv2 = torch.nn.Conv2d(8, 16, kernel_size=1, stride=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        return (torch.mm(input1, input2)) + torch.mm(input3, input4)

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
