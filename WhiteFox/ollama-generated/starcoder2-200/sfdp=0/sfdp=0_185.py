
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y2):
        return torch.matmul(x1, y2) / 0.78649373

 # Initializing the model
m = Model()
 # Inputs to the model
x1 = torch.randn(16, 50)
y2  = torch.randn(16, 50)

__output__  = m(x1, y2)

