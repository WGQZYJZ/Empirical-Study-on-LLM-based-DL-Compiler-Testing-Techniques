This pattern characterizes scenarios where the dot product of two tensors is computed, then scaled by a scalar, then softmax is applied, then dropout is applied, and finally the dot product of the dropout output and a value tensor is computed. This is a typical pattern found in the attention mechanism of Transformer models.


# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        m = torch.nn.Linear(x_size_1, z)  # Create a linear layer (fully connected) to map from input of size x_size_1 to latent space of dimension z
        return m(x1)


# Inputs to the model
x1 = torch.randn(256, 3, 64, 64)
