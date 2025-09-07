
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(8 * 32, 16)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = torch.relu(v1) 
        return v2

m = Model()

 # Inputs to the model