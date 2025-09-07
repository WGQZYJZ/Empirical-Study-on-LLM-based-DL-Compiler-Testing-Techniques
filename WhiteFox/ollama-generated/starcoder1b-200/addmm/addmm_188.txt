
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Linear(10, 12)
 
    def forward(self, x1, inp=None):
        v1 = self.m1(x1) + inp  # Add the result of the matrix multiplication to another tensor 'inp'
        return v1


# Initializing the model
m = Model()


