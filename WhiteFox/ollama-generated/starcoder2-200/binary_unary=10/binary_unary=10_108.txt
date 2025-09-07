
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 84 * 96, 51)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor
        v3 = torch.relu(v2)

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(768, 96, 51, 84, 32)
__output__  = m(x1)
