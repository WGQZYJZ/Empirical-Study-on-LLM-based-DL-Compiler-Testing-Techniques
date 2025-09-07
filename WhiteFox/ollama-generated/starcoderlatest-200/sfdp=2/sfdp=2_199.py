
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, q, k, v, query_mask=None, key_padding_mask=None, attention_mask=None):
        qk = torch.matmul(q, k.transpose(-2, -1)) # Compute the dot product of a query and a key
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by an inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(v) # Compute the dot product of the dropout output and a value
        return output


# Initializing the model
m = Model()

# Inputs to the model
q  = torch.randn(1, 3, 64, 64) # (batch_size x embedding_dim x qk_len x embed_dim)
k  = torch.randn(1, 3, 64, 64) # (batch_size x embedding_dim x qk_len x embed_dim)
v  = torch.randn(1, 3, 64, 64) # (batch_size x embedding_dim x qk_len x embed_dim)
query_mask = None #(batch_size x query_length x query_length)
key_padding_mask = None #(batch_size x key_length x query_length)
attention_mask  = None # (batch_size x seq_length x seq_length)
