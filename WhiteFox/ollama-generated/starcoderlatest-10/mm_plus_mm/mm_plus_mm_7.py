
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul1 = torch.nn.Linear(2, 4)
        self.matmul2 = torch.nn.Linear(3, 5)
 
    def forward(self, x1):
        v1 = torch.mm(x1, self.matmul1.weight) + torch.mm(x1, self.matmul1.bias) # Matrix multiplication between input and weight matrix of the first linear layer followed by addition with bias
        v2 = torch.mm(x1, self.matmul2.weight) + torch.mm(x1, self.matmul2.bias) # Matrix multiplication between input and weight matrix of the second linear layer followed by addition with bias
        v3 = v1 + v2
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2)
