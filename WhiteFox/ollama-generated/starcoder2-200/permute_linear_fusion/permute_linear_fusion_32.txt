
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x):
      v1  = torch.nn.functional.relu(x).permute(-1, -2, -3) # Relu first then permute the last 3 dimensions of the input tensor
      v2  = self.linear(v1)
      return v2

# Initializing the model
m  = Model()

