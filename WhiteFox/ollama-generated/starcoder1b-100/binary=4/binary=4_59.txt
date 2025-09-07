
class Model(torch.nn.Module):
    def __init__(self, linear_layer):
        super().__init__()
        self.linear = torch.nn.Linear(in_features=784, out_features=10)
 
    def forward(self, x1):
        v1 = self.linear(x1) + 2
        return v1


# Initializing the model
m  = Model(torch.nn.Linear)


# Inputs to the model
x1 = torch.randn(1, 784)
