
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1024, 512)

    def forward(self, x3):
        v8  = self.linear(x3)
        return v8

# Initializing the model
m  = Model()

 # Inputs to the model
  x3  = torch.randn(64, 70, 512)
  __output__  = m(x3)
 
