
class Model(torch.nn.Module):
    def __init__(self, args):
        super().__init__()
        self.embed = torch.nn.Embedding(vocab_size, embed_dim)
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        # Inputs to the model
        key = self.embed(x2)
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it
        attn_mask = torch.ones(x2.shape[:-1] + (self.num_attn, ))  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        value = self.embed(x1)
        output = attn_weight @ value  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
model = Model(args)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 32, 32)
