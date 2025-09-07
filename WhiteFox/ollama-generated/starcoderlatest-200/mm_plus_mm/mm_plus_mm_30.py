
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 5)
        self.conv2 = torch.nn.Conv2d(3, 8, 3)
 
    def forward(self, x1, x2, x3, x4):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = torch.mm(v1, v2) + torch.mm(x3, x4) # Matrix multiplication between the results of the two pointwise convolutions and the input tensors to these two pointwise convolutions
        return v3


# Initializing the model
m = Model()


