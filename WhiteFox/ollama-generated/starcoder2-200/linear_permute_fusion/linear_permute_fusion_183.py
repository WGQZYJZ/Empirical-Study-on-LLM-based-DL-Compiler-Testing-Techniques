
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         v3 = torch.nn.functional.linear(x1, self.weight) 
         v4  = v3.permute([0, 2, 1])  
         return v4

# Initializing the model
m = Model()

 # Inputs to the model: 3 x 5 x 7
x1 = torch.randn(3, 5, 7)

__output__  = m(x1)

