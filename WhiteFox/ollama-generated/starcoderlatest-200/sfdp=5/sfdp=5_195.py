
class MultiheadAttention(torch.nn.Module):
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        self.num_heads = num_heads

        # Calculate the dimension of the keys, queries, values, and output for each head
        self.key_dim = embed_dim // num_heads
        self.query_dim = embed_dim // num_heads
        
        self.attn = torch.nn.Linear(self.key_dim + self.query_dim,
                                    num_heads * (self.key_dim + self.query_dim))

        # Calculate the dimension of each head
        self.value_dim = num_heads * (self.key_dim + self.query_dim)

    def forward(self, x1, x2, v1):
        b, n, c = x1.shape  # Batch size, sequence length and number of features

        qk = torch.cat((x1, x2), dim=-1).view(b * (n - 1),
                                              self.key_dim + self.query_dim)
        attn_weight = self.attn(qk).view(b, n - 1,
                                          self.num_heads, self.value_dim)

        attn_weight = attn_weight.permute(0, 2, 1, 3)
        
        # Calculate the softmax of scaled dot product and multiply attention weights with value
        output = torch.bmm(attn_weight, v1)
        
        return output

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multihead = MultiheadAttention(320, 16)
 
    def forward(self, x1, x2, v1):
        return self.multihead(x1, x2, v1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 480, 960, 960) # Batch size 2 and length of each sequence
v1 = torch.randn(2, 480, 320, 960) # Value embeddings (i.e., the key-value matrix V from transformer models). For transformer models, this should be different from the previous one.
