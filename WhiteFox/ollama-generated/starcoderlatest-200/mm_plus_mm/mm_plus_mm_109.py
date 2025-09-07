
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.pool = torch.nn.MaxPool2d(kernel_size=4, stride=1, padding=0, ceil_mode=False)
 
    def forward(self, x1):
        v1 = torch.mm(input1, input2)
        v2 = torch.mm(input3, input4)
        v3 = v1 + v2
        return self.pool(v3)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
