
class AttentionModel(torch.nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.attn = torch.nn.Linear(2 * hidden_size, 3)
 
    def forward(self, x1, x2):
        v1  = x1 @ x2.transpose(-2, -1) / math.sqrt(x1.size(-1)) # Compute the dot product of two tensors, and scale it
        v1  = v1 + torch.eye(v1.size(-1)).to(v1).unsqueeze(0).repeat((v1.size(0), 1, 1))[:, :, None, :].to(x2) # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(v1, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        return v1 @ attn_weight.transpose(-2, -1).unsqueeze(-1) # Compute the dot product of the dropout output and the value
# Initializing the model
m = AttentionModel()
attn_output = m(x1, x2)

