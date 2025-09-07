
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, y2):
        v1 = self.conv(x1) + y2  # Add a tensor to the output of the convolution and then apply ReLU
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
y2 = torch.rand_like(x1, requires_grad=True)
