

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1)
 
    def forward(self, x):
        x0 = x
        x1  = self.conv1(x)
        x_splitted, _   = torch.split(x1, [4, 5], dim=3) # Split the output of convolution into two tensors along dimension 3. 
        x2  = self.conv2(x0)
        x3  = torch.cat([x2] * len(x_splitted), dim=len(x_splitted))
        return [x1, x_splitted[0], x_splitted[1]]
        return (x3, [v for v in [x1, x_splitted[0], x_splitted[1]] if v is not None])

# Initializing the model
m  = Model()

# Inputs to the model.
__inputs__   = torch.randn(1, 3, 64, 64)

__outputs__ = m(__inputs__)

