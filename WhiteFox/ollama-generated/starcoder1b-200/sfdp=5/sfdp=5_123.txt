
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        k1 = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it
        attn_mask = torch.FloatTensor(k1.shape).zero_() # Create a FloatTensor to fill with zeroes
        attn_mask[:, 0] = 1.0  # Set the diagonal of the attention mask to one, so we don't divide by a NaN
        attn_mask += (1 - query) * (1 - key)  # Add an attention mask to prevent division by zero
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        v = attn_weight @ value  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()

