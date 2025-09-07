
class AttentionModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.attention_layer = torch.nn.Linear(768, 1)
 
    def forward(self, query, key, value, attn_mask):
 
        # Step 1: compute the dot product of the query and key vectors
        qk = (query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1))
 
        # Step 2: add the attention mask to the scaled dot product in order to ignore the padding tokens
        qk = qk + attn_mask
 
        # Step 3: apply softmax over all query and key vectors
        attn_weights = torch.softmax(qk, dim=-1)
 
        # Step 4: compute the dot product of attention weights and value vectors
        attn_output = (attn_weights @ value).transpose(-2, -1)
 
        return attn_output
 
    def __repr__(self):
        return self.__class__.__name__

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.att = AttentionModule()
 
    def forward(self, query, key, value, attn_mask):
        attn_output = self.att(query, key, value, attn_mask)
        return attn_output


# Initializing the model
m = Model()

# Inputs to the model
input_ids = torch.randn((1, 256, 768), dtype=torch.long)
attn_mask = torch.eye(256).unsqueeze(0) > 0
 
