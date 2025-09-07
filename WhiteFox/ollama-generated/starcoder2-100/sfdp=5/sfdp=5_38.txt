
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, attn_mask3):
        v1 = torch.softmax(query1 @ key2.transpose(-2, -1) / math.sqrt(query1.size(-1)), dim=-1) + attn_mask3  # Compute the dot product of the query and key, add it with the attention mask, then apply softmax to the result
        v2 = torch.dropout(v1, dropout_p=0.5, train=True) * value  # Multiply the output of softmax by a constant, then multiply this result by another constant
        return v2


# Initializing the model