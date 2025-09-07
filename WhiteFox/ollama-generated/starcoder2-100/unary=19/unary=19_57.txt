
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28*28, 10)
 
    def forward(self, x):
         v3 = self.linear(x).view(-1, 10)
         v4 = torch.sigmoid(v3)
         return v4
 
# Initializing the model
m  = Model()

 # Inputs to the model
x  = torch.randn(64, 28*28)
 
 __output__  = m(x)

