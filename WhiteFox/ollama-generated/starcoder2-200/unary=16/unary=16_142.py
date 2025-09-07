
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v1 = self.lin1(x1)
        v2 = F.relu(v1) 
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(32) # Shape: [batch_size]
