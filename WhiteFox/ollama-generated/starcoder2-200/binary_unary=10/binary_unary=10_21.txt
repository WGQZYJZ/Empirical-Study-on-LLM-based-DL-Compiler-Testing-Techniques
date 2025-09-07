
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + other
        v3 = torch.relu(v2) # You can use torch.nn.functional.relu to simplify
        return v3


# Initializing the model
m  = Model()
 
