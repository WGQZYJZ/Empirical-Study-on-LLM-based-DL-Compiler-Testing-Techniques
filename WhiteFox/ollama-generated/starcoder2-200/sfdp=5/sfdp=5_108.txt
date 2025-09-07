
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(256, 128)
        self.key = torch.nn.Linear(256, 128)
        self.value = torch.nn.Linear(256, 128)

    def forward(self, x):
      k = self.query(x) @ self.key.transpose(-2,-1) / math.sqrt(self.query(x).size(-1)) 
      v = self.value(x)
      a = torch.softmax(k + 0.3, -1)
      a = torch.dropout(a, 0.5, True)
      o = a @ v
      return o


# Initializing the model
m = Model()

 # Inputs to the model
x = torch.randn(24, 256)
