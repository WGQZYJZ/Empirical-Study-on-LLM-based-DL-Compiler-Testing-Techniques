
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(64 * 64, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = F.sigmoid(v1)
        v3  = v1 * v2
        return v3

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(64, 64)
x2 = torch.randn(64, 50)
x3 = torch.randn(1, 597)
 
# Output of the model on inputs x1 and x2:
__output__  = m((x1, x2))
 
# Output of the model on input x3 is different from that obtained above for both inputs x1 and x2:
__output___ = m(torch.randn(64))

