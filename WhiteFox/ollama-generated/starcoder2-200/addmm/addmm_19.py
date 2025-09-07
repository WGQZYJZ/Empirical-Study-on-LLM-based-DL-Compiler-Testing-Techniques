
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.functional.linear

    def forward(self, inp):
         v1  = torch.mm(inp[0], inp[1])
         return [v1] + ['out1', 'out2']

 # Initializing the model
m = Model()
 
 # Inputs to the model
x1  = [torch.randn(3), torch.randn(4)]
  