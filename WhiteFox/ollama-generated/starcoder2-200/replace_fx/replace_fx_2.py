

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
      t1  = torch.nn.functional.dropout(x1, p=0) # Apply dropout to the input tensor with probability 0
      t2 = torch.rand_like(t1, dtype=torch.float64) + \
            (x1 > torch.nn.functional.dropout(x1)) / 5

      return x1 - t2

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(3, 20)

# Forward pass
__output__= m(x1)
