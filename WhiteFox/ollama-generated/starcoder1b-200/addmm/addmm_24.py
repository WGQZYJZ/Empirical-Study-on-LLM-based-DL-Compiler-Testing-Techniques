
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=10):
        v1 = torch.mm(x1, x2) + inp  # Pass `inp` as a keyword argument to the `torch.mm` operation
        return v1


# Initializing the model
m = Model()


