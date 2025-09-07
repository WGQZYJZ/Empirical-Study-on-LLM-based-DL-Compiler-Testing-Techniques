
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmult = torch.nn.Linear(10, 8)
 
    def forward(self, x):
        v1  = self.matmult(x[0]) + x[2] # Multiply the input by a matrix and then add another tensor to it
        return v1

# Initializing the model
m = Model()

