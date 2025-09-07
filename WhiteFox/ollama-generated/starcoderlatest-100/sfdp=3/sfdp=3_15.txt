
class Model(torch.nn.Module):
    def __init__(self, input_dim=512, key_dim=2048, head_dim=16384, num_heads=8):
        super().__init__()
        self.multihead_attention = MultiHeadAttention(input_dim, key_dim, head_dim, num_heads)
 
    def forward(self, query, key):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()


