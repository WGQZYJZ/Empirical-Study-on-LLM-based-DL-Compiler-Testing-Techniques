
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
       v = torch.cat([x1, x2], dim=0) # Concatenate two input tensors along 0 dimension
       v = v.view(-1) # Reshape the concatenated tensor with 1 dimension, which is now a vector.
       v = torch.nn.functional.relu(v) # Apply ReLU to this vector.
       return v

# Initializing the model
m  = Model()

