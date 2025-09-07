
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = torch.nn.Linear(784, 30)
 
    def forward(self, x):
        return self.lin1(x + x)


m  = Model() # Initialize the model
x1  = torch.randn(5, 784)  # Input tensor
__output__  = m(x1)