
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(32, 80, 45, 95)


# Outputs of the model
__output__  = m(x1)

# Results: The outputs of your generated models should be valid PyTorch tensors, whose shapes match the specified values in the description.