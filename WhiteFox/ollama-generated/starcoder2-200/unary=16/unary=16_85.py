
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x2):
        v2  = self.linear(x2)
        v3  = F.relu(v2) 
        return v3


# Initializing the model
m  = Model()
 
 # Inputs to the model
 x2 = torch.randn(1, 784)
 __output__  = m(x2)
