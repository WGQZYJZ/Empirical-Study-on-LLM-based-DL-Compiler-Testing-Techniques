
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, attn_mask, dropout_p=0.1):
        qk = (x1 @ x2.transpose(-2, -1)) / torch.sqrt((x1.size(-2)) * (x2.size(-2)))
        qk = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight = F.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        v = (attn_weight @ x2).transpose(-2, -1)
        return v


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
attn_mask = torch.zeros((1, x2.size(-2), x2.size(-2))) # Generate an attention mask for the values of `value`
