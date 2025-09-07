
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(512, 3)
 
    def forward(self, x):
        v1 = F.linear(x, torch.rand(512, 3)) 
        v2 = F.relu(v1) 
        return v2

 # Initializing the model
 m = Model()
 
 # Inputs to the model
 x = torch.randn(64, 512) 
 __output__  = m(x)
