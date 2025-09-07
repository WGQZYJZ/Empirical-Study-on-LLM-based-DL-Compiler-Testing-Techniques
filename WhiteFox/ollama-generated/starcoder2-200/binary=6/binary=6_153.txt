
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 - other # The tensor 'other' is provided by the user and will be added to the output of linear transformation here
        
        return v2


# Initializing the model
m = Model()
 
