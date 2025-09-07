
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 5)
 
    def forward(self, x):
        v1  = self.linear(x) # Linear transformation
        v2  = v1 + 3 # Addition operation 
        v3  = F.relu6(v2) # Apply ReLU6 activation function
        return torch.div(torch.clamp(v3, min=0), max=6)


# Initializing the model
m  = Model()
 

# Inputs to the model
x1 = torch.randn(1, 5)

 __output__  = m(x1)
 
