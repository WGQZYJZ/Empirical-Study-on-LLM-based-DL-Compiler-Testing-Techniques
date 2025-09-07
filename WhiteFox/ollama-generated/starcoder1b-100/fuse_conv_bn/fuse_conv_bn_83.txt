
class Module(torch.nn.Module):
    def __init__(self, weight=None, bias=None):
        super().__init__()
        self.weight = weight
        self.bias = bias

    def forward(self, input_tensor):
        return torch.conv2d(input_tensor, 
                          self.weight, 
                          stride=1, 
                          padding=0) + self.bias


# Inputs to the model
x1 = torch.randn(1, 2, 5, 7)
