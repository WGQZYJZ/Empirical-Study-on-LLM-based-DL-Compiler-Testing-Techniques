
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, inp):
        v1 = torch.mm(x1, input2)
        return v1 + inp

 # Initializing the model
 m  = Model()
 
 # Inputs to the model
  x1  = torch.randn(4096, 576)
  inp = torch.randn(3072, 576)
  