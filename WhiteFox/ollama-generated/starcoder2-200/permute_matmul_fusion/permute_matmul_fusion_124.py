

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
      v1 = torch.randn(5, 3) # or torch.rand()... 
      # ...or something else that you think can be used as the input tensor.
      return torch.bmm(v1, torch.permute(x2, -1, 0))

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3,) # or any other tensor that can be used as the input for v1
x2  = torch.randn(5, 6) # or another one

