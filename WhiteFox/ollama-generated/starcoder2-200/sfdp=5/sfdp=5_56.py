
class MyModel(torch.nn.Module):
    def __init__(self, dim: int = 128) -> None:
        super().__init__()
        self.linear1 = torch.nn.Linear(dim, dim*2)

    def forward(self, x):
      output = torch.relu_(x)
      output = self.linear1(output)
      return output

model = MyModel()


# Inputs to the model
input_tensor  = torch.ones((30, 4))
__output__    = model(input_tensor)