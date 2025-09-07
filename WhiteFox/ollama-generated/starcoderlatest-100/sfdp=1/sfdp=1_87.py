
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        # Add code here to compute dot product of the query and key tensors, then scale it by an inverse scale factor (for numerical stability), apply softmax function, dropout the output tensor.
        return None


# Inputs to the model
query = torch.randn(10, 8)
key = torch.randn(10, 16)
value = torch.randn(10, 32)
