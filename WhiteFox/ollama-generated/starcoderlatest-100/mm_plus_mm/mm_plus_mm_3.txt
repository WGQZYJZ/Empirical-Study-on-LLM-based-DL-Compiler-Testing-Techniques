
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul1 = torch.nn.Linear(5, 4)
        self.matmul2 = torch.nn.Linear(3, 7)
 
    def forward(self, x1):
        v1 = self.matmul1(x1)
        v2 = self.matmul2(x1)
        v3 = v1 + v2
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 5, 4)
