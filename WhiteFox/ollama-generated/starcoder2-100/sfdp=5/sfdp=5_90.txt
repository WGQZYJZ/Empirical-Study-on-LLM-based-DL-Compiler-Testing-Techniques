
class MultiHeadedAttention(torch.nn.Module):
    def __init__(self, n_head=8, d_model=128):
        super().__init__()
        self.d_k = 64
 
        # Compute the number of queries in each layer by dividing the d_model size with the number of heads 
        # and computing the residual module using it as a parameter value
        self.residual_module = torch.nn.Sequential(torch.nn.Linear(self.d_k, self.d_k), 
                                                   torch.nn.ReLU(), 
                                                   torch.nn.Linear(self.d_k, self.d_k))
 
        self.n_head = n_head
 
    def forward(self):
        # Generate random tensor of shape [batch, query] as a query
        query = torch.randn(20, self.residual_module[1].in_features)
        key  = torch.randn(20, 64*8)
 
        mask = torch.ones([query.size(-1), k.size(-1)])
        # Generate random tensor of shape [batch] as an attention mask 
        attn_mask = torch.randint(0, self.n_head, (self.residual_module[0].in_features,))
 
        # Compute the dot product of the query and key by adding it to the attention mask
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) + attn_mask
 
        # Apply softmax to the result 
        attn_weight = torch.softmax(qk, dim=-1)
        output  = self.residual_module[0](attn_weight @ value)
        return output

# Initializing the model
m  = MultiHeadedAttention()

