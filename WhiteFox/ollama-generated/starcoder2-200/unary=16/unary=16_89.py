
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3 * 64 * 64, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = F.relu(v1) # A PyTorch module to apply the ReLU activation function on input values. 
        return v2


# Initializing the model
m2  = Model()

# Inputs to the model
x2  = torch.randn(1, 3 * 64 * 64)

__output2__ = m(x2)