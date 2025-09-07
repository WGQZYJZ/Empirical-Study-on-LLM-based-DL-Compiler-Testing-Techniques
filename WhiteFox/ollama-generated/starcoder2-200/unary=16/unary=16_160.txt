
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(3072, 1536)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = F.relu(v1) 
        return v2
# Initializing the model
m  = Model()
# Inputs to the model
x1 = torch.randn(3072).reshape(-1, 64, 9) # Change the shape of an input tensor based on your requirements


