
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 25)
 
    def forward(self, query, key, value):
        # Compute the dot product of a query tensor and a key tensor 
        # Compute the dot product of a query tensor and a key tensor, scale it by a constant, then apply softmax to the scaled dot product
        # Compute the dot product of the result and a value tensor.
        v1 = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of two tensors 
        v2 = self.linear(v1)
        v3 = query @ k @ v2  # Multiply query with key and then multiply the result by another tensor.

        return v3


# Initializing a model instance for testing:
m = Model()

# Create some inputs to pass to your forward method of the model:
x1 = torch.randn(5, 10)
x2 = torch.randn(5, 10)
x3 = torch.randn(5, 25)


