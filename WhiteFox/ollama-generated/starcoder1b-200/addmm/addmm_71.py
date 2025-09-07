
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Linear(20, 2, bias=True)
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp) + 5  # Pass 'inp' as a keyword argument to the matrix multiplication operation
        return v1


# Initializing the model
m = Model()


