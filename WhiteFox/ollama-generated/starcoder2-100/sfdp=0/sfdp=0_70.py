
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale=None):
 
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale # Scaled dot product attention
        attention_weights   = scaled_dot_product.softmax(dim=-1)                 # Softmax for self-attention
        output              = attention_weights.matmul(value)                    # Weighted sum of the value tensors
 
        return  output

# Initializing the model and passing arguments
m = Model()
 
query = torch.randn([32,64])   # Random query tensor with 32 samples and 64 dimensions per sample
key = torch.randn(1000,[32, 8])         # Random key/query pair of size [batch_size x key_length x dim] for the transformer model
value = torch.randn([32,8])                  # Random value tensor with 32 samples and 64 dimensions per sample

inv_scale = query.size(-1) ** -0.5                # Inverse scaling factor

__output__  = m(query, key, value, inv_scale=inv_scale)

