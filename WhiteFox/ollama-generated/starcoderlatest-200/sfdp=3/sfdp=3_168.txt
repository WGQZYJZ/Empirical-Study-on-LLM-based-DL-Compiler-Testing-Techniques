
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_layer = torch.nn.MultiheadAttention(num_heads=8,
                                                             embed_dim=64,
                                                             dropout=dropout)
 
    def forward(self, query, key, value):
        qk  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk * scale_factor # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk * value # Compute the dot product of the dropout output and the value tensor
        return output

# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 3, 64, 64) # query is a matrix whose shape should be (batch_size=1, num_heads=8, sequence_length=None, head_dim=64). You need to set sequence_length=None if you don't know the length of each sequence.
key = torch.randn(1, 3, 64, 64) # key is a matrix whose shape should be (batch_size=1, num_heads=8, sequence_length=None, head_dim=64). You need to set sequence_length=None if you don't know the length of each sequence.
value = torch.randn(1, 3, 64, 64) # value is a matrix whose shape should be (batch_size=1, num_heads=8, sequence_length=None, head_dim=64). You need to set sequence_length=None if you don't know the length of each sequence.
