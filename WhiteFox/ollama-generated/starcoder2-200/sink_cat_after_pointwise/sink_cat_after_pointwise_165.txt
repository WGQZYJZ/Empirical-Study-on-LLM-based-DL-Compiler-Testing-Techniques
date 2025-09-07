
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):  # Input tensors should be of shape [batchsize, dim]
        v = torch.cat([x1, x2], dim=1)  # Concatenate input tensors along dimension 1
        v = v.view(-1, 3).reshape(v.shape[0])  # Reshape concatenated tensor and flatten the output
        v = torch.relu(v)  # Apply ReLU pointwise unary operation to reshaped tensor
        return v


# Initializing the model
m = Model()


# Inputs to the model (Tensor type: torch.Tensor, Shape: [batchsize] )