

class TransformerAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(d_model, d_k)  # Key/Value projections
        self.key = torch.nn.Linear(d_model, d_k)  # query = 3
        self.value = torch.nn.Linear(d_model, d_k)
 
    def forward(self, query):
        inv_scale  = math.sqrt(self.key.weight.shape[-1])
 
        query_projection  = self.query(query) 
        key_projection  = self.key(query) 
        value_projection  = self.value(query) 
 
        scaled_dot_product = torch.matmul(query, key_projection.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
 
        return query_projection + attention_weights

# Initializing the model