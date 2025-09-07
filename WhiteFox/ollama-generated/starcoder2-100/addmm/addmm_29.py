
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Linear(784, 10)
 
    def forward(self, inp=None):
        v2 = self.mm(inp) + self.mm(inp) # Add the result of matrix multiplication twice on 'inp' tensor
        return v2


# Initializing the model
m = Model()
