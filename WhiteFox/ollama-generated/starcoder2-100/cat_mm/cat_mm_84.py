
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1  = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        t1  = torch.mm(x1, torch.randn(784, 50))
        t2  = torch.cat([t1 for i in range(10)])
        return self.layer1(t2)


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(64, 784).float().requires_grad_(True) # Input tensor of 784 elements, each of them is a float value. 

# Output of the model using inputs x1 and m
__output__  = m(x1)

