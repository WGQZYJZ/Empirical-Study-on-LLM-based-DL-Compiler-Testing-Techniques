
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_linear1 = torch.nn.Linear(3072, 512)
        self.attn_linear2 = torch.nn.Linear(512, 8)
 
    def forward(self, query, key, value, attn_mask):
        v1 = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        v1 = v1 + attn_mask
        v2 = torch.softmax(v1, dim=-1)
        v3 = v2 @ value
        return v3


# Initializing the model
m = Model()

# Inputs to the model
attn_mask = torch.randn(8, 3072).sigmoid_() # The attention mask used in ScaledDotProductAttention module is an 8-dimensional Tensor of type float and with random values from 0 to 1.
query = torch.randn(8, 3072) # The input query tensor has size (batch_size, num_heads * head_dim). It contains a batch of linear queries for each attention head in the form `(batch_size, embed_dim)`.
key = torch.randn(32, 3072) # The input key tensor has size (batch_size, num_heads * head_dim). It contains a batch of linear keys for each attention head in the form `(batch_size, embed_dim)`.
value = torch.randn(8, 3072) # The input value tensor has size (batch_size, num_heads * head_dim). It contains a batch of linear values for each attention head in the form `(batch_size, embed_dim)`.


# 