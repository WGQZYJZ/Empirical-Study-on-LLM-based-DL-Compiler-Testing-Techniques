
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.conv = torch.nn.Conv2d(16, 16, 3, stride=1)
        self.linear1 = torch.nn.Linear(1920, 576)
        self.linear2 = torch.nn.Linear(576, 1)
        self.dim = dim
 
    def forward(self, x):
        v1 = self.conv(x).view(-1, int(x.size()[1] * x.size()[2] * x.size()[3])) # Perform a linear transformation and reshape the result into a 2D tensor with size 2464 for input of dimension dim to the second hidden linear layer
        v2 = self.linear1(v1)  # Firstly apply the first linear transformation with an output size of 576 on the reshaped data
        v3 = self.linear2(v2) # Apply a second linear transformation on the result of the previous step to produce the final output
        return v3


# Initializing the model
m = Model(dim=16)


# Inputs to the model
x = torch.randn(4, 3, 64, 64)
