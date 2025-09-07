
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.nn.functional.dropout(x1, 0.5)
        v4 = torch.nn.functional.linear(v3, self.linear.weight, self.linear.bias)
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.rand(10)

 __output__  = m(x1) 
