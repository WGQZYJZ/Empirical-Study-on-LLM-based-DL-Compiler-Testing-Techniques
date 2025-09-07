
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=dropout_p)
        self.linear1 = torch.nn.Linear(dim, dim)
        self.linear2 = torch.nn.Linear(dim, num_heads * size_per_head)
        self.layer_norm1 = torch.nn.LayerNorm(dim)
        self.layer_norm2 = torch.nn.LayerNorm(num_heads * size_per_head)
 
    def forward(self, q, k, v):
        qk = torch.matmul(q, k.transpose(-2, -1))  # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = self.dropout(softmax_qk)  # Apply dropout to the softmax output
        output = torch.matmul(dropout_qk, v)  # Compute the dot product of the dropout output and the value
        output = output.transpose(-2, -1).contiguous()  # Transpose output to be of shape (batch_size, seq_len, dim)
        output = self.layer_norm1(output + q)  # Layer norm on intermediate output
        output = output.view(*output.shape[:3], -1)  # Flatten to (batch_size, seq_len, num_heads * size_per_head)
        output = self.linear2(self.layer_norm2(output))  # Feed linear layer to produce the output
        return output


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(1, dim, seq_len)
k1 = torch.randn(1, dim, num_heads * size_per_head)
v1 = torch.randn(1, dim, num_heads * size_per_head)
