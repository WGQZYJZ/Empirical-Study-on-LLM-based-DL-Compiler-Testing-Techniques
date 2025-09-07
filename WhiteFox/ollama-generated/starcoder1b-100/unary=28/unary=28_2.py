
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 6)
 
    def forward(self, x1, **kwargs):
        v1 = self.linear(x1)
        v2 = v1 + kwargs['min_value']
        v3 = v2 + kwargs['max_value']
        return v3


# Initializing the model
m  = Model()


