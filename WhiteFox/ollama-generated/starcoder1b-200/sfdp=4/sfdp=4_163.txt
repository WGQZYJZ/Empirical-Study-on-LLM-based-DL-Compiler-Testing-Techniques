
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        kq  = (x1 @ x2.transpose(-2, -1)) / math.sqrt(x1.size(-1))
        attn_mask = self.attention_mask_(x2.shape[-2:])  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ x2  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

