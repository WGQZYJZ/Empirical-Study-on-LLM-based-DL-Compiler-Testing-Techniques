
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(32,8)
 
    def forward(self, x1):
        v1  = self.fc(x1) 
        v2 = torch.sigmoid(v1)
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(32)
 
# Getting a single output from the model
__output_single__  = m(x1)[0]

