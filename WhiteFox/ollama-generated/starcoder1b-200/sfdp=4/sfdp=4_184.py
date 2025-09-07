
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        qk = self.query @ self.key.transpose(-2, -1) / math.sqrt(self.key.size(-1))
        attn_mask = torch.triu(torch.ones(qk.shape[-1], kq.shape[-1]))  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ self.value
        return output


# Initializing the model
m = Model()


