
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.weight) # Apply linear transformation to the input tensor.
        return v1.permute(-2, -3, 0, 1).sum()


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 4, 5) # Tensor with shape (batch_size, feature, sequence_length), where batch_size is arbitrary and feature/sequence length depends on the particular data set being examined.
__output__  = m(x1)

