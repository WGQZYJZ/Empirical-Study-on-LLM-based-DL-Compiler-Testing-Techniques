
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
 
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(20, 3) # An input tensor of shape (N, M), where N is a positive integer and M is a positive integer
 
 