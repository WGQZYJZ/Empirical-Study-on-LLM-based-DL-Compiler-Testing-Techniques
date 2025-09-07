
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*56*56, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.sigmoid(v1)

        return v2


# Initializing the model
m  = Model()
# Inputs to the model
x1  = torch.randn(300*56*56, 8)

 # Generating input_tensors for generating output tensors with public APIs


__output__  = m(x1)

