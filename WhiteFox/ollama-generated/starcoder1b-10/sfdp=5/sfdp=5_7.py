
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        w1 = torch.zeros_like(v1)
        attn_mask = self.attn_mask(w1).unsqueeze(-2).expand(*w1.size())
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # The dot product between the query and key is then divided by sqrt(key.size(0)), to prevent overflows caused by float division
        attn_weight = torch.softmax(qk, dim=-1) # Softmax along dimension 1 of both qk and attn_mask
        qk = attn_weight @ value # The attention weights are then multiplied by the output from the dropout
        output = qk @ mask * v1 + (1 - mask) * v1.clone() # We apply an operation called masking on the result of the softmax function to remove the influence of the attention
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
