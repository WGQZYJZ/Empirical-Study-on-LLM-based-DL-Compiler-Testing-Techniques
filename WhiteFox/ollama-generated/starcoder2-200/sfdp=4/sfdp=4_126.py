
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):
         qk = torch.bmm(query, torch.transpose(key, -2, -1)) / math.sqrt(float(key.size(-1)))
         qk += attn_mask
         att_weight  = torch.softmax(qk, dim=-1)
         output  = torch.bmm(att_weight, value)
         return output

# Initializing the model