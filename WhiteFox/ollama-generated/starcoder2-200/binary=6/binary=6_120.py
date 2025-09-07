
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.linear = torch.nn.Linear(96*7504/1, 32)
 
    def forward(self, x1):
        v1 = conv(x1)
        v2 = linear(v1.view(-1)) # view(-1) is used to flatten the input tensor
        return v2


# Initializing the model
m2 = Model()

# Inputs to the model