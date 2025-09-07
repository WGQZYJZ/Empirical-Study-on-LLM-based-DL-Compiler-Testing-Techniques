
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3,8)
 
    def forward(self, x1):
        v2  = torch.sigmoid(self.linear(x1))
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(4096,3) # The input tensor must have size [N, F], where N is the number of data points and F is the number of input features.
__output__  = m(x1)

