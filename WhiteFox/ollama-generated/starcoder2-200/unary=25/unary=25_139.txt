

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(784, 10)
 
    def forward(self, x):
        v1  = self.linear(x.view(-1, 784))
        v2  = (v1 > 0).type_as(torch.FloatTensor())
        v3  = -0.5 * negative_slope # noqa
        v4  = torch.where(v2, v1, v3)
 
        return v4

# Initializing the model
m  = Model()
 
# Input to the model
x  = torch.randn(64, 784)
 
