
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value, attn_mask=None, dropout_p=0.1):
        qk = torch.bmm(query, key.transpose(-2,-1)) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)   # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p=0.1, inplace=True)    # Apply dropout to the softmax output 
        output  = torch.bmm(attn_weight, value).float()   # Compute the dot product of the dropout output and the value
        return output

# Initializing the model with randomly generated query/key/value tensors for demonstration purposes only. The model should be different from the previous one.
query = torch.randn((1024, 768))
key   = torch.randn((512, 768))
value = torch.randn((1024, 512))
 
m  = Model()

