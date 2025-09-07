
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout  = torch.nn.Dropout(p=0.5)

    def forward(self, x1):
      v1  = torch.nn.functional.dropout(x1, p=0.4) # original dropout
      # new random tensor
      v2  = torch.rand_like(v1)
      return (v1, v2)

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(20, 5)
# __output__  = m(x1)

