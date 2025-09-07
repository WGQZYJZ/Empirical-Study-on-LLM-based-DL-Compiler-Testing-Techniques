
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(64*64*8, 64)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 + other  # Add another tensor to the output of the linear transformation
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x = torch.randn(256, 3, 64, 64)
