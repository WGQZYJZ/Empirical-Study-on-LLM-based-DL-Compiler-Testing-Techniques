
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, scale_factor=None, dropout_p=0.1):
        # Input shape: [batch, seq_len, dim] or [batch, dim]
        # Output shape: [batch, seq_len, dim]
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of query and key tensors
        if scale_factor is not None:
            scaled_qk  = torch.mul(qk, 1 / (scale_factor ** 0.5))  # Scale the dot product by a factor
        else:
            scaled_qk  = qk
 
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)  # Apply softmax to the scaled dot product

        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = torch.bmm(dropout_qk, value)   # Compute the dot product of the dropout output and a value tensor
        return output


# Initializing the model
m  = ScaledDotProductAttention()
 
 
