
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.nn.functional.dropout(x1 + 3., p=0.5) 
        return v2

 # Initializing the model
 m = Model()
 
 # Inputs to the model
  x1  = torch.ones((1, 2))

 