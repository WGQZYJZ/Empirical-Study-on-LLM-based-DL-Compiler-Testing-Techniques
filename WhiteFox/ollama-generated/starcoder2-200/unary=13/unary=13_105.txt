
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1280, 4096)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v3  = self.relu(v1) * v1
        return v3

# Initializing the model
m = Model()

 # Inputs to the model
 x2 = torch.randn(7048, 56 * 90 + 192 + 96)
 __output__  = m(x2)
