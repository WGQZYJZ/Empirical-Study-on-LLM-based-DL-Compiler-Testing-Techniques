
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, d_model, num_heads, dropout=0):
        super().__init__()
        self.d_model = d_model
        self.num_heads = num_heads
        self.w_qs = torch.nn.Linear(d_model, num_heads * d_model)
        self.w_ks = torch.nn.Linear(d_model, num_heads * d_model)
        self.w_vs = torch.nn.Linear(d_model, num_heads * d_model)
 
        self.layer_norm_attention  = torch.nn.LayerNorm(d_model)
        self.dropout1 = torch.nn.Dropout(p=dropout)
        self.dropout2 = torch.nn.Dropout(p=dropout)
 
    def forward(self, query, key, value):
        batch_size = query.shape[0]
 
        q = self.w_qs(query).view(batch_size, -1, self.num_heads, self.d_model // self.num_heads).permute(0, 2, 1, 3)
        k = self.w_ks(key).view(batch_size, -1, self.num_heads, self.d_model // self.num_heads).permute(0, 2, 1, 3)
        v = self.w_vs(value).view(batch_size, -1, self.num_heads, self.d_model // self.num_heads).permute(0, 2, 1, 3)
 
        q = self.dropout1(q)
        k = self.dropout1(k)
        v = self.dropout1(v)
 
        attn_output = torch.matmul(q, k.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        attn_output = attn_output / (float(self.d_model) ** 0.5) # Scale the dot product by 1 / sqrt(d_k)
 
        attn_output = torch.nn.functional.softmax(attn_output, dim=-1) # Apply softmax to the scaled dot product
        attn_output = self.dropout2(attn_output)
 
        output = torch.matmul(attn_output, v) # Compute the dot product of the dropout output and the value tensor
 
        output = output.permute(0, 2, 1, 3).contiguous() # Reshape to (batch_size, num_heads, seq_len, d_model / num_heads)
        output = output.view(batch_size, -1, self.d_model)
 
        output = self.layer_norm_attention(output + query) # Apply layer normalization to the output tensor
 
        return output


# Initializing the model
m = MultiHeadAttention(32, 4)
 

# Inputs to the model
query = torch.randn(6, 10, 32)
key = torch.randn(5, 10, 32)
value = torch.randn(7, 10, 32)


