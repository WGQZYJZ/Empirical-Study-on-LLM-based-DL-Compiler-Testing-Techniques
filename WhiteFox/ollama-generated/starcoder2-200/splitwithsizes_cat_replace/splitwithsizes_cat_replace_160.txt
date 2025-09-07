
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
      return  torch.split(x1, [1], dim=0)

# Initializing the model and running the split function with input_tensor as an argument to it:

model = Model()

 