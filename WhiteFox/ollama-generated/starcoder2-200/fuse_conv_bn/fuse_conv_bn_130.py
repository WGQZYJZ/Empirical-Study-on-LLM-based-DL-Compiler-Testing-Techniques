
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, kernel_size=1)

    def forward(self, x1): 
        v1 = torch.nn.functional.conv2d(x1, weight=self.conv.weight, bias=self.conv.bias, stride=None, padding=None, dilation=None)
        v2  = torch.nn.functional.batch_norm(v1, weight=self.conv.weight, bias=None, running_mean=None, running_var=None, momentum=0.1, eps=9e-05)

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(4, 3, 28, 28)
 
 