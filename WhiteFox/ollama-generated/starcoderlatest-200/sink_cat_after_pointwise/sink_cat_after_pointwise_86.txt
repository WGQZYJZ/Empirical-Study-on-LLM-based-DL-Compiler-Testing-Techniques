
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1, x2):
        t1  = torch.cat([x1, x2], dim=1) # Concatenate input tensors along the second axis
        v2  = t1.view(-1, 4)           # Reshape the concatenated tensor to a tensor with shape (batch_size * sequence_length, embedding_dim)
        t3  = torch.relu(v2)          # Apply a pointwise unary operation to the reshaped tensor
        return t3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(80, 4)
x2 = torch.randn(80, 4)
