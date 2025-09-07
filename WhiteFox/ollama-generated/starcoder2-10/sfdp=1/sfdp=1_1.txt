
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, value1):
        v1  = torch.matmul(query1, key1.transpose(-2, -1))
        v2  = v1 / inv_scale_factor
        v3  = v2.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=dropout_p)
        __output__  = v4.matmul(value1)
        return __output__


# Initializing the model with some parameters
m  = Model()
 
query1  = torch.randn(batch, num_heads, query_len, d_model // num_heads) / np.sqrt(d_model)
key1    = torch.randn(batch, num_heads, key_len, d_model // num_heads) / np.sqrt(d_model)
value1  = torch.randn(batch, num_heads, value_len, d_model // num_heads) / np.sqrt(d_model)
 
 
