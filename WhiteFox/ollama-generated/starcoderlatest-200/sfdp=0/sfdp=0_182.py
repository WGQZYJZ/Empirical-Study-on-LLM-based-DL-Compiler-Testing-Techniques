
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.attention = torch.nn.MultiheadAttention(embed_dim=1024)
 
    def forward(self, query, key, value, attention_mask):
        # compute scaled dot product of the attention matrix and query
        attention_scores  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(key.shape[-1])
 
        # softmax to obtain probability distribution over head dimension
        attention_weights = F.softmax(attention_scores, dim=-1)
 
        # get weighted average of value vector corresponding to each head
        # this is equivalent to the element-wise multiplication of the attention weights and value vectors
        output  = torch.matmul(attention_weights, value)
 
        return output, attention_weights

# Initializing the model
m = Model()


