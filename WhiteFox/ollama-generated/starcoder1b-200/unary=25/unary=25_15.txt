
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.where(v1 > 0, v1, - v1) # For each element in v1, if the corresponding element is True, the corresponding element from v1 is chosen, otherwise it's negative value of v1 is chosen
        return v2


# Initializing the model
m = Model()


