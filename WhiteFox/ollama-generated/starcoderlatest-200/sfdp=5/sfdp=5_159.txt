
class MultiheadAttention(torch.nn.Module):
    def __init__(self, embed_dim, num_heads=8, dropout=0., scale=False):
        super().__init__()
        if scale:
            self.fc_q = torch.nn.Linear(embed_dim, embed_dim * 3)
            self.fc_k = torch.nn.Linear(embed_dim, embed_dim * 3)
            self.fc_v = torch.nn.Linear(embed_dim, embed_dim * 3)
        else:
            self.fc_q = torch.nn.Linear(embed_dim, num_heads * embed_dim)
            self.fc_k = torch.nn.Linear(embed_dim, num_heads * embed_dim)
            self.fc_v = torch.nn.Linear(embed_dim, num_heads * embed_dim)
        self.dropout = torch.nn.Dropout(dropout)
 
    def forward(self, query, key, value):
        # The output dimension of the multihead attention layer is equal to 3 times the embedding dimension
        q = self.fc_q(query).view(*query.size()[:-1], -1)
        k = self.fc_k(key).view(*key.size()[:-1], -1)
        v = self.fc_v(value).view(*value.size()[:-1], -1)
 
        # The output of the linear transformation should be divided by sqrt(embedding dimension), because a dot product between two vectors will be scaled by the square root of its norm. 
        q, k, v = [torch.nn.functional.relu(x, True) for x in (q, k, v)]
        q *= query.size(-1) ** -0.5
        k *= key.size(-1) ** -0.5
        v *= value.size(-1) ** -0.5
 
        attn_weight = torch.matmul(q, k.transpose(-2, -1)) # Perform a dot product between the query and the keys in the dimension of embedding dimension
        attn_mask = (key != 0).unsqueeze(3).expand(*attn_weight.size())
        attn_weight += attn_mask

        attn_weight = self.dropout(attn_weight) # Perform dropout
        output = torch.matmul(attn_weight, v)
        output = output.view(*output.size()[:-1], -1)
 
        return output


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multihead_attention = MultiheadAttention(32)
 
    def forward(self, x1):
        qk  # Output of the multihead attention layer
        return self.multihead_attention(x1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 32, 64, 64)
