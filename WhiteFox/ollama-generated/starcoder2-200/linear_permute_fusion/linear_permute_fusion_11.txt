
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)  # Apply linear transformation to the input tensor.
        v2 = v1.permute(0, -1, -2).squeeze(-1)  # Permute the output tensor from the linear transformation and squeeze the last dimension (to convert the 3D tensor into a 2D one).
        return v2

# Initializing the model
m = Model()

# Inputs to the model. The input is a 5-d torch.Tensor with size 1 x 4096 x 7 x 88 x 25, which corresponds to the batch_size=1 (1-d), embedding dimensionality= 4096 (2-d), sequence length = 7 (3-d) and 88 classes.
x1  = torch.randn(1, 4096, 7, 88, 25) # A random input tensor of size 1 x 4096 x 7 x 88 x 25

 __output__  = m(x1).shape

# Model and inputs: 313
