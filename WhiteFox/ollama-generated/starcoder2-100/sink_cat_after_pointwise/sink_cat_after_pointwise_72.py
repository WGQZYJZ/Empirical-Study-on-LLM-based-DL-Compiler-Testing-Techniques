
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1, t2):
      t3 = torch.cat([t1, t2], dim=0) # Concatenate the input tensors along a dimension and then reshape the concatenated tensor.
      t4 = t3.view(-1, 4)
      v5 = F.relu(t4) 
      return v5

# Initializing the model
m = Model()

