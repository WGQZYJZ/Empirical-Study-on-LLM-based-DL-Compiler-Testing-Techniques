
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, scale_factor, dropout_p=0.1):
        v = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        inv_scale_factor = 1 / scale_factor # Inverse scale factor
        scaled_v = v * inv_scale_factor # Scale the dot product by the inverse scale factor
        softmax_v = scaled_v.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_v = torch.nn.functional.dropout(softmax_v, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_v.matmul(key) # Compute the dot product of the dropout output and the key tensor
        return output


# Initializing the model
m = Attention()

