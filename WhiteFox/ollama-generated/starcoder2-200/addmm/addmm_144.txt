
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(784, 50) # Construct a linear layer of size (784, 50)
        self.linear2 = torch.nn.Linear(50, 10) # Construct another linear layer of size (50, 10)

    def forward(self, x):
        v1 = torch.mm(x.view(-1), self.linear1.weight.t()) 
        v2 = self.linear1(v1)
        v3 = self.linear2(v2)
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x = torch.randn(64,784)

__output__  = m(x)
