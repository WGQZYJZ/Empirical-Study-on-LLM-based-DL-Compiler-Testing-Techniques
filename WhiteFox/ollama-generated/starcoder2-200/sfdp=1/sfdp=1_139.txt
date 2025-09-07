
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x):
        v1  = torch.matmul(x, self.linear.weight) + self.linear.bias
        v2  = torch.nn.functional.gelu(v1)
        return v2


# Initializing the model
m  = Model()
 
 # Inputs to the model
x = torch.randn(30, 10) 
 