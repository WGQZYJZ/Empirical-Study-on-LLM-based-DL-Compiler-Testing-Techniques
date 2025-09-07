
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = Attention()
 
    def forward(self, x1, x2):
        query  = torch.cat((x1, x2), dim=-1) # Combine the inputs as a sequence
        key     = torch.cat((x1, x2), dim=-2) # Combine the keys as a sequence
        attn_mask = self.attn(query, key)  # Compute the attention weights (and an attention mask)
        output   = self.attn(query, key) @ x2  # Perform the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()


