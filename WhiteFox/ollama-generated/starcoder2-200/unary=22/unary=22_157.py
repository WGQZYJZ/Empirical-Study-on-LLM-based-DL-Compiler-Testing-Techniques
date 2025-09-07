
class Model(torch.nn.Module):
    def __init__(self, dim1=32, dim2=32):
        super().__init__()
        self.fc  = torch.nn.Linear(dim1 * dim2 + 4096, dim2)
 
    def forward(self, x1):
        v1  = self.fc(x1)
        return torch.tanh(v1)


# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(320, 64 * 64)
 
 __output__  = m(x1).reshape(-1)
