
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        return torch.full([x.shape[0], x.shape[1], 2], 3, dtype=dtype)

 # Creating the model
m = Model()

 # Input to the model
