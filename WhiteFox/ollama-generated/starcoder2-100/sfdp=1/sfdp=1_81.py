
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x0):
        v1 = torch.matmul(x0, self.linear.weight) + self.linear.bias
        return v1

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(4, 32)
