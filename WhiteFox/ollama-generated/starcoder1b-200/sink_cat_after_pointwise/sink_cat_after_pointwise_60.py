
class Model(torch.nn.Module):
    def __init__(self, dropout):
        super().__init__()
        self.dropout = dropout

    def forward(self, x1):
        t1  = x1.permute(0, 2, 1)
        t2  = torch.cat([tensor1, tensor2, ...], dim=...)  # Concatenate tensors along a dimension
        t3  = t1.view(...)  # Reshape the concatenated tensor
        t4  = torch.relu(t2)  # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        t5  = self.dropout(t4)  # Do dropout here

        return t5


# Initializing the model
m = Model(torch.nn.Dropout2d())


