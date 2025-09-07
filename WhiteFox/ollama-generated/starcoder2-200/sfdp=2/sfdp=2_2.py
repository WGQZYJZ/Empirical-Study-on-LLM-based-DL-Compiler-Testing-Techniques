
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1):
        v1  = torch.matmul(q1, key.transpose(-2, -1)) 
        v3 = v1 * inv_scale_factor
        v4  = scaled_qk.softmax(dim=-1)
        v5 = torch.nn.functional.dropout(v4, p=p)
        v6  = v5.matmul(value)
        return v6

# Initializing the model
m  = Model()

 # Inputs to the model
 q1  = torch.randn(batch_size * num_heads, seq_length, d_model // num_heads) 
 key  = torch.randn(batch_size * num_heads, d_model//num_heads, d_k) 
 value  = torch.randn(batch_size*num_heads, seq_length, d_model // num_heads)
 p  = 0.5
 