
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul  = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        v3  = self.matmul(x1)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(256, 3072)
