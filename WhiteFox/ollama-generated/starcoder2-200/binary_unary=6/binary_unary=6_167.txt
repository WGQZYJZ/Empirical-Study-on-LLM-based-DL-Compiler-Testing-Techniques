
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(4096, 8192)
 
        other = torch.randint(-350, 350).item()
 
        self.other = other
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = v1 - self.other
        v3  = F.relu(v2)
        return v3


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(4, 6075, device="cuda")
 
 # Running the model in GPU environment
