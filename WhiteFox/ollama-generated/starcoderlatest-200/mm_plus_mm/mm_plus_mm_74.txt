
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = torch.nn.Linear(1024, 512)
 
    def forward(self, x1):
        t1 = torch.mm(x1, x1.t())  # A single matrix multiplication is performed
        t2 = torch.mm(x1, x1.t())  # Another single matrix multiplication is performed
        t3 = t1 + t2  # Both of the matrix multiplications results are added together
        return self.layer1(t3)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1024)
