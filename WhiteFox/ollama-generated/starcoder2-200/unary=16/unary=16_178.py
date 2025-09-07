
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3*64*64, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.relu(v1)
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
input_tensor = torch.randn(1, 3*64*64)
output   = m(input_tensor)
