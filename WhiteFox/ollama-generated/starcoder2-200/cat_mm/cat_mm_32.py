
class Model(torch.nn.Module):
    def __init__(self, m1=3, m2=5):
        super().__init__()
        self.linear = torch.nn.Linear(m1, 8)
 
    def forward(self, x1):
        v1  = x1
        v1  = self.linear(v1).detach()
        return v1


# Initializing the model and its parameters (assuming the number of input and output tensors are fixed).
m = Model(42)

 # Inputs to the model
x1  = torch.randn(3, 5)

