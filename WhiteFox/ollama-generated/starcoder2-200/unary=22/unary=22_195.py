
class Model(torch.nn.Module):
    def __init__(self, hidden_size=1024):
        super().__init__()
        self.linear  = torch.nn.Linear(784, hidden_size)
        self.tanh = torch.nn.Tanh()
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = self.tanh(v1) 
        return v2

# Initializing the model 
m  = Model()

 # Inputs to the model 
x1 = torch.randn(32,784)
__output__= m(x1)
 

# Model 2: ReLU Activation Function
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        v = torch.relu(v) 
        return v

 # Inputs to the model 
x1= torch.randn(32,784)
__output__= m(x1)
