
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v1  = self.conv(x1) + other_tensor
        v2  = self.relu(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 8, 64, 64)
other_tensor  = torch.randn(10, 5, 10, 7).requires_grad_()
__output__  = m(x1)

