
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(512*7*7, 4096)
        self.relu   = torch.nn.ReLU()
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = v1 + other_tensor
        v3  = self.relu(v2)
        return v3


# Initializing the model
m  = Model()
 
 # Inputs to the model 
 x   = torch.randn(5, 512*7*7)
 other_tensor = torch.rand(4096)
 __output__   = m(x)