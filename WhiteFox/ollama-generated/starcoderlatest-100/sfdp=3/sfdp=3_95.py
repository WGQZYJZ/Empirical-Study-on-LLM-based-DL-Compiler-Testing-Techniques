
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.d_key, self.d_value = 3 * d_model // num_heads, 2 * d_model // num_heads
 
        # We can define the parameter of the matrix multiplication operation here
        self.scaled_attention_linear = torch.nn.Linear(self.d_key + self.d_value, d_model)
        self.dropout = torch.nn.Dropout()
 
    def split_head(self, x):  # Split the feature dimension into `num_heads` parts
        batch_size, seq_len, _ = x.shape
        return x.view(batch_size * (seq_len // self.num_heads), self.num_heads, self.d_key)
 
    def forward(self, query, key):  # Multi-head attention is performed here
        batch_size, seq_len, _ = query.shape
 
        if seq_len % self.num_heads != 0:
            raise ValueError('Query and key length must be a multiple of the number of heads')
 
        x1 = torch.cat([query, key], dim=2) # Concatenate the feature dimensions of the two tensors
        x2 = self.split_head(x1)  # Split the feature dimensions into `num_heads` parts
 
        scaled_qk  = self.scaled_attention_linear(x2).view(batch_size, -1, seq_len) # Dot product with query and key matrices
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = self.dropout(softmax_qk)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(self.split_head(key)) # Compute the dot product of the dropout output and the key tensor
 
        return output.view(batch_size, seq_len, -1).contiguous() # Concatenate feature dimensions back into a single tensor


class Model(torch.nn.Module):
    def __init__(self, n_heads):
        super().__init__()
        self.multiheadattention = MultiHeadAttention(512, 4)
 
    def forward(self, x):
        v1 = self.multiheadattention(query=x, key=x)
        return v1


# Inputs to the model
m = Model(n_heads=8)
x1 = torch.randn(4, 32, 512)
