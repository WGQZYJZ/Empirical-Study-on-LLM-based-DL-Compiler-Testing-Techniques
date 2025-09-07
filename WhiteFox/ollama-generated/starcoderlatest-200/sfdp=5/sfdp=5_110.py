
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensor, query, key, attn_mask):
        # compute qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        # add the attention mask
        qk = torch.matmul(query, key.permute(0, 1, 3, 2).contiguous()) / math.sqrt(key.size(-1)) + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        # apply dropout to the softmax output and finally compute the attention weights and the output
        attn_weight = torch.dropout(attn_weight, 0.25, True)
        output = torch.matmul(attn_weight, value).contiguous()
        return output


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(1, 3, 64, 64)
query = torch.randn(1, 8, 64, 64)
key = torch.randn(1, 8, 64, 64)
attn_mask = torch.ones((1, 1, 64, 64))
