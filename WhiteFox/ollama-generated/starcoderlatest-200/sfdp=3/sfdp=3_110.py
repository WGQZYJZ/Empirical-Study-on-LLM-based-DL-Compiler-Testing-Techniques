
class Model(torch.nn.Module):
    def __init__(self, query_dim, key_dim, value_dim, num_heads=16):
        super().__init__()
        self.query_linear = torch.nn.Linear(query_dim, query_dim)
        self.key_linear = torch.nn.Linear(key_dim, key_dim)
        self.value_linear = torch.nn.Linear(value_dim, value_dim)
        self.num_heads = num_heads
 
    def forward(self, query, key, value):
        scaled_qk  = (torch.matmul(query, self.query_linear.weight).unsqueeze(-1) + 
                      torch.matmul(key, self.key_linear.weight)) / math.sqrt(query.shape[-1]) 
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.p) # Apply dropout to the softmax output

        # The dot product of query and value tensor is computed.
        dot_product  = torch.matmul(dropout_qk, self.value_linear.weight).squeeze(-1) 
        scaled_dot  = dot_product * math.sqrt(self.num_heads)
        attn_output = scaled_dot + query
        
        return attn_output

# Initializing the model
m = Model(query_dim=768, key_dim=768, value_dim=3072, num_heads=16)

# Inputs to the model
x1 = torch.randn(batch_size, 5, 768)
