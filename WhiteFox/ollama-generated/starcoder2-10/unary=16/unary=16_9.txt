
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1000, 4)
    
    def forward(self, x):
        v1 = self.linear(x)
        v2 = F.relu(v1)
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model 
 input_data = torch.randn(64, 1000)
