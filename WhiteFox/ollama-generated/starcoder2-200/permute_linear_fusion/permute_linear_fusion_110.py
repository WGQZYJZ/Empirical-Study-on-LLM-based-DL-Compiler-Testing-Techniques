
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x):
        v0  = x.permute(-1, -3).reshape(-1, 8)
        v1  = torch.nn.functional.linear(v0, self.linear.weight, self.linear.bias)
        return v1

# Initializing the model
m = Model()

 # Inputs to the model
x  = torch.randn(32, 4) 
 __output__  = m(x)