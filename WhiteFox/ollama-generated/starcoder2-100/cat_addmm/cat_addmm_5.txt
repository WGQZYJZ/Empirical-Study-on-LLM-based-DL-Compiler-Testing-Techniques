
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
 
        self.linear1 = torch.nn.Linear(784, 256)

        self.relu = torch.nn.ReLU()

    def forward(self, x): 
        v1 = self.linear1(x)
        v2 = self.relu(v1)
        return t3


# Initializing the model
m = Model(dim=0)


# Inputs to the model
inputs  = torch.rand(64, 784)
__output__  = m(inputs)
 
