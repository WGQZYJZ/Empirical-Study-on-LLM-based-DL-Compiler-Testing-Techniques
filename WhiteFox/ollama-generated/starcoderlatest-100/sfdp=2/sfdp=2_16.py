
class Attention(torch.nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.proj = torch.nn.Linear(input_dim, input_dim)
 
    def forward(self, query, key, value):
        # Query: Tensor of shape [batch size x # queries x dim].
        # Key: Tensor of shape [batch size x # keys x dim].
        # Value: Tensor of shape [batch size x # keys x dim].
        batch_size = query.shape[0]
        input_dim = query.shape[-1]
 
        qk  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value
 
        return output


# Initializing the model
m1 = Attention(64 * 256)
x1  = torch.randn(batch_size, num_heads, x_dim, x_dim) # [batch size x num head x x dim x x dim]


