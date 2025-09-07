
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v4  = v1 + other_tensor  # The variable `other` contains a constant, 1 for example 
        v2 = torch.relu(v3)

# Initializing the model
m = Model()


# Inputs to the model
__output__  = m(x1)

