
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256 * 4, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.sigmoid(v1)
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(500, 3 * 4* 4)
 
# Running the model on inputs x1 and printing the output.
__output__  = m(x1)

