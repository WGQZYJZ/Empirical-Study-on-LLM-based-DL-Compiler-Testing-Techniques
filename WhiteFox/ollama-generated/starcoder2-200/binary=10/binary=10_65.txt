
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x1):
        return (x1 + self).sum()

 # Initializing the model
m = Model()
 
 # Inputs to the model 
 input_tensor  = torch.randn(32, 50)
  __output__  = m(input_tensor)
 
