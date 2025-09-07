
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v1_attention = (v1 * 0.5).unsqueeze(-1) @ v1.unsqueeze(2).unsqueeze(3)  # Compute the dot product of the query and key and scale it
        qk = v1_attention + (0.5 - attn_mask)  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        output = attn_weight @ value  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()


