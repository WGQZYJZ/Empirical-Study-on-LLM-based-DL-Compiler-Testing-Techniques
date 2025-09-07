
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_layer = torch.nn.Linear(704, 1)
 
    def forward(self, x):
        return self.linear_layer(x) * 2


# Initializing the model
m = Model()


