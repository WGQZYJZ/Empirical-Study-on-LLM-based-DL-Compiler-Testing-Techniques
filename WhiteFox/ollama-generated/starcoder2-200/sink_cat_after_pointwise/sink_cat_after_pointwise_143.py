
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1):
      t2 = torch.cat([t1[0], t1[1]], dim=3)
      t3 = t2.view(-1, 9).clamp(min=-5, max=5) # Apply clamp to the reshaped tensor after a concatenation along axis 3 (which is also the batch dimension)
      return torch.relu(t3)


# Initializing model
model = Model()
# Inputs for the model
inputs1 = [torch.ones((1, 4, 5)), torch.zeros((1, 6))]
