
class Model(torch.nn.Module):
    def __init__(self, embed_dim):
        super().__init__()
        self.query = torch.nn.Linear(embed_dim, 1)
        self.key   = torch.nn.Linear(embed_dim, 64 * 257, bias=False)
 
    def forward(self, query):
 
        v3  = self.query(query).permute(-1,-2).contiguous().view(257, -1) # Flatten the result of applying a linear layer to the query and permute it
        attn_mask = torch.ones([257]*3, device="cpu")  # Generate an attention mask
        attn_mask[0][-1]   = float("-inf")
 
        attn_weight  = self.key(query).softmax(-1) * attn_mask 
        attn_weight  = torch.dropout(attn_weight, 0.12589254117941673, True) 
        v4           = v3 @ attn_weight.permute((-2,-1)).contiguous().view(-1,v3.size(-1))  # Compute the dot product of the flattened result and the softmax output
        return torch.nn.Tanh()(v4).tanh()


# Initializing the model