
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 4, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        return (v2 + v1) / 2


# Initializing the model
m = Model()


# Inputs to the model
__input_tensor__ = torch.randn(1, 3, 64, 64)
x1 = __input_tensor__.cuda().contiguous()
x2 = x1 * 0.5
x3 = x1 * -1.0
t1 = torch.mm(__input_tensor__, __input_tensor__) # Matrix multiplication between input and input
t2 = torch.mm(x3, x2) # Matrix multiplication between input and input
t3 = t1 + t2
