
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(480016, 2)
 
    def forward(self, x1): 
        v1 = F.linear(x1, weight=self.weight) 
        v2 = F.relu(v1) 
        return v2

# Initializing the model
m  = Model()
 
# Input to the model
x1  = torch.randn(1000,480016) # Size of input: 1000 * 480016
__output__   = m(x1)

