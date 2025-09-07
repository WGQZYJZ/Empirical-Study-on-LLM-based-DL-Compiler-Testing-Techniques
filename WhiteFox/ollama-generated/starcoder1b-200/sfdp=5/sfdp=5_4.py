
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        query = torch.randn(1, 3, 64, 64) # The shape of `query` is (1, 3, 64, 64), which matches the input tensor's shape.
        key   = torch.randn(2, 8, 64, 64) # The shape of `key` is (2, 8, 64, 64), which also matches the input tensor's shape.
        value = torch.randn(1, 3, 64, 64)
        mask  = torch.ones((1, 2, 64, 64)) # The shape of `mask` is (1, 2, 64, 64). It should have the same shape as `query` and `key`.
        attn_weight  = torch.softmax(torch.bmm(query, key.transpose(-2, -1)), dim=-1) # Apply softmax to the dot product of the two tensors.
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output.
        attn_output  = torch.bmm(attn_weight, value) # Compute the output as the result of a batched matrix multiply.
        return attn_output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # The shape of `query` is (1, 3, 64, 64), which matches the input tensor's shape.
key   = torch.randn(2, 8, 64, 64) # The shape of `key` is (2, 8, 64, 64), which also matches the input tensor's shape.
value = torch.randn(1, 3, 64, 64)
