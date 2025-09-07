
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         v1 = torch.nn.Linear(3, 8)(x1)
         v2 = v1 + 5
         return v2

 # Initializing the model
 m = Model()

 # Inputs to the model
 x1 = torch.randn(1, 3) 
 __output__=m(x1)

