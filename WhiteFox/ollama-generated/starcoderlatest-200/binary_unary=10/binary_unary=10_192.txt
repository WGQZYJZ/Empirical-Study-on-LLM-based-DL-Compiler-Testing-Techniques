
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        v1 = self.conv(x1) + t2 # Add another tensor to the output of the linear transformation
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
