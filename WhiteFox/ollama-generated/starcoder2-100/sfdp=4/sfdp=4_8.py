

class MultiHeadAttention(torch.nn.Module):
    def __init__(self, d_model=768, num_heads=12):
        super().__init__()
 
        self.d_k = d_model // 32 # Compute the size of the hidden dimension used in the multi-head attention. For Transformer models with 1024 dimensions for each hidden layer and a total of 768 hidden layers, this value is 32.
        self.n_heads = num_heads
 
        self.q_proj = torch.nn.Linear(d_model, d_model) # Create a linear transformation for the query
        self.k_proj = torch.nn.Linear(d_model, d_model) # Create a linear transformation for the key
        self.v_proj = torch.nn.Linear(d_model, d_model) # Create a linear transformation for the value

        self.output  = torch.nn.Linear(d_model, d_model)
 
    def forward(self, query, key, value):
        qk  = self.q_proj(query).reshape(len(query), -1 ,32, 768//32)//self.n_heads # Apply the linear transformations to the query and compute a multi-head scaled dot product
        k   = self.k_proj(key).reshape(-1, len(value), self.d_model)
        v   = self.v_proj(value).reshape(-1,len(value),self.d_model)
 
        qk  = torch.einsum('...ij,...ik->...jk',qk, k) # Compute the dot product of query and key for each dimension in the last two axes
        attn_mask = torch.tril(torch.ones((len(query), len(value)), dtype=torch.bool), diagonal=-1).to(query.device) # Create an attention mask with entries for diagonal elements on the diagonal and 1 on the upper triangular matrix of zeros below that
        attn_mask = torch.where(attn_mask == False, torch.tensor(-np.inf, dtype=torch.float32), torch.zeros((len(query), len(value)),dtype=torch.float32)) # Replace the values in the attention mask corresponding to diagonal elements with -Infinity
        attn_weight = F.softmax(qk + attn_mask, dim=-1)  # Compute the softmax of query-key multiplied by the attention mask 
        output   = torch.einsum('...jk,...ik->...ij',attn_weight, v) # Compute a weighted sum of value using the attention weights
        return self.output(output).reshape(-1,len(value),d_model)
 
attention  = MultiHeadAttention()

