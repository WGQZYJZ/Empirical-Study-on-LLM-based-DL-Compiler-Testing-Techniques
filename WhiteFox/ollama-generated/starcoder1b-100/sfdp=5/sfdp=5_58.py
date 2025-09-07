
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        qk = x1 @ x2.transpose(-2, -1) / math.sqrt(x1.size(-1))  # Compute the dot product of the query and key, and scale it
        attn_mask = self._attn_dropout(torch.ones(x1.shape), dropout_p)  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = self._attn_dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        return attn_weight @ x2


# Initializing the model
m = Model()


