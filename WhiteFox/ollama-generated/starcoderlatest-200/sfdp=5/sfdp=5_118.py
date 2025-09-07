
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_layer = torch.nn.MultiheadAttention(embed_dim=8, num_heads=1)
 
    def forward(self, x1, x2):
        qk  = self.attention_layer(x1, x2, x2)[0] # Compute the dot product of the query and key, and scale it
        qk  = qk + torch.ones((64,64)).to(device)[:,:,:,None].to(torch.float32).repeat(1, 1, 1, 64*5) # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        output = attn_weight @ self.attention_layer.v  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m2 = Model2()

