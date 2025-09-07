
class AttentionModel(torch.nn.Module):
    def __init__(self, d_model, n_head):
        super().__init__()
        self.d_model  = d_model
        self.n_head   = n_head
 
        self.query = torch.nn.Linear(d_model, d_model) 
        self.key = torch.nn.Linear(d_model, d_model)
        self.value = torch.nn.Linear(d_model, d_model)
 
    def forward(self, query: torch.Tensor):
        attn_mask  = torch.triu(torch.ones((query.size(-1), query.size(-1))), diagonal=0).bool()
        vq  = self.query(query) 
        vk  = self.key(query)
        vv  = self.value(query)
        qk  = vq @ vk.transpose(-2, -1) / math.sqrt(self.d_model) # Compute the dot product of the query and key (plus an attention mask)
        attn_weight = torch.softmax(qk + attn_mask.to(torch.float), dim=-1)  # Apply softmax to the result 
        output  = attn_weight @ vv 
        return output

# Initializing the model
model  = AttentionModel(d_model, n_head)

