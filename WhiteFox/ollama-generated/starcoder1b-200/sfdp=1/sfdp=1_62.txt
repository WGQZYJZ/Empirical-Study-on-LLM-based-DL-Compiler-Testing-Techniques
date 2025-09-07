
class Model(torch.nn.Module):
    def __init__(self, key_size=8, num_heads=1, bias=False):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(
            num_heads=num_heads, dropout=dropout_p, batch_first=True)  # Construct the attention layer
        self.layer_norm = torch.nn.LayerNorm(epsilon=1e-6, elementwise_affine=bias)
        self.dense = torch.nn.Linear(key_size + num_heads * key_size, value_size, bias=False)
 
    def forward(self, x1, x2):
        # First compute the dot product of the query and key tensors
        v  = self.attention(x1, x2, x1)[0]  # Apply the attention layer to the input
        scaled_v = v.div(self._get_inv_sqrt_scale_factor(x1))  # Scale the dot product by the inverse of sqrt(batch size)
        softmax_v = F.softmax(scaled_v, dim=-1)  # Apply softmax to the scaled dot product
        dropout_v = F.dropout(softmax_v, p=dropout_p)  # Apply dropout to the softmax output
        x3  = self.layer_norm(x2 + torch.matmul(dropout_v, x1))  # Compute the layer normalization and the additive term from the dot product of the dropout output and the input tensor
        x4 = F.softmax(self.dense(x3), dim=-1)  # Apply softmax to the summation between the input vector and the weights matrix
        return x4


# Initializing the model
m = Model()


# Inputs to the model
query_vector = torch.randn(2, 1, 64, 64)
key_vector = torch.randn(2, 3, 8, 8)
