
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask):
        qk  = torch.einsum('ibc, jbc -> ijb', [query / math.sqrt(query.size(-1)), key])  # Compute the dot product of the query and key tensors
        attn_weight = torch.softmax(qk + attn_mask)  # Compute the attention weights using softmax and the added attention mask
        output = torch.einsum('ijb, bcd -> icd', [attn_weight, value])  # Compute the dot product of the attention weights and the value tensor
        return output

# Initializing the model
m  = ScaledDotProductAttention()


# Inputs to the model
query = torch.randn(4, 300, 8)
key = torch.randn(4, 512, 8)
value = torch.randn(4, 512, 64)
attn_mask = torch.zeros(4, 512, 512).fill_(torch.inf)
__output__  = m(query, key, value, attn_mask)

