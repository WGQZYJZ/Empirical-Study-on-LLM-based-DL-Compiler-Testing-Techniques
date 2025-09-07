
class Model(torch.nn.Module):
    def __init__(self, attn_mask):
        super().__init__()
        self.attn_mask = attn_mask
 
    def forward(self, query, key, value):
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk  = qk + self.attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        return attn_weight @ value # Compute the dot product of the dropout output and the value

    def generate_attention_mask(self):
        batch_size = 16
        seq_length = 48

        attention_mask = torch.zeros((batch_size, seq_length, seq_length))
        for i in range(0, batch_size):
            j = random.randint(1, seq_length-2)
            k = random.randint(1, seq_length-2)
            if j <= k:
                attention_mask[i][j][k] = 1 # Fill the mask
        attention_mask = torch.unsqueeze(attention_mask, dim=0).to(device) # Add the batch dimension

        return attention_mask
# Initializing the model and passing in the attention mask (with only one sample and sequence of size 48 for testing)
m = Model(attn_mask=attn_mask)
m.eval()


# Inputs to the model
query  = torch.randn(1, 3, 64, 64).to(device)
key    = torch.randn(2, 3, 64, 64).to(device)
value  = torch.randn(2, 3, 64, 64).to(device)


# 