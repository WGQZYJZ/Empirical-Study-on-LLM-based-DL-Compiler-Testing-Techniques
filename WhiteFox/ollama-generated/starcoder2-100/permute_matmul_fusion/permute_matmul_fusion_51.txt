
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
      v1 = torch.permute(x1)  # permute the input tensor A and B 
      v2 = torch.bmm(v1, x2)   # or torch.matmul(v1, x2), call the bmm/matmul function.
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 2, 3)  # random inputs for the input tensor A (the shape should be [batch_size, sequence length, hidden size])
x2  = torch.randn(1, 4, 5)  # random inputs for the input tensor B (the shape should be [batch_size, sequence length, hidden size])
__output__  = m(x1, x2)

