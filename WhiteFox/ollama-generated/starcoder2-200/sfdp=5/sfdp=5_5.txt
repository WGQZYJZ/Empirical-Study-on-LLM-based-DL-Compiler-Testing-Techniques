
class Attention(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
 
        self.attn = torch.nn.Linear(config["hidden_size"], config["hidden_size"])

    def forward(self, query, key, value, attn_mask=None): 
        v1  = self.attn(query) # Apply the dot product of the query and the attention matrix
        if(attn_mask is not None):
            v2  = v1 + attn_mask # Add the attention mask to the scaled dot product
        else: 
            v2 = v1
        v3  = torch.softmax(v2, dim=-1) # Apply softmax to the result
        v4  = torch.dropout(v3, config["hidden_size"], True) 
        return v4 @ value


# Initializing the model
attn = Attention({ "hidden_size": 65 })
 
# Input tensors for the attention module
query  = torch.randn(10, 7, 92, 38) # 10 batches of size 7*38*92
key  = torch.randn(10, 7, 46, 52) # 10 batches of size 7*46*52
value = torch.randn(10, 7, 46, 52) # 10 batches of size 7*46*52
 
# Attn mask (optional) for attention module
attn_mask = torch.tensor([[[[ -inf ]]]])


__output__  = attn(query, key, value, attn_mask)

