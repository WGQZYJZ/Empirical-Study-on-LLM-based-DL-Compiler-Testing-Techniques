
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(256, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + 0 
        v3  = F.relu(v2) # Using F.relu() instead of torch.nn.ReLU()
        return v3

# Initializing the model
m  = Model()

