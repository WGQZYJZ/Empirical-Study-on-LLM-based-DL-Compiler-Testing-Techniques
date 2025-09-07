
class Model(torch.nn.Module):
    def __init__(self, *args):
        super().__init__()
        self.linear = torch.nn.Linear(*args)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2 = v1 - other # Subtract 'other' from the output of the linear transformation
        return v2


# Initializing the model
m = Model()


