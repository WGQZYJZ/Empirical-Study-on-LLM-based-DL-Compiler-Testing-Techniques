
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
      v1  = torch.nn.functional.dropout(x1, p=0.5) # Apply dropout to the input tensor
      v2  = torch.rand_like(v1) # Generate a tensor with the same size as v1 filled with random numbers
      
      return v2

# Initializing the model
m  = Model()

