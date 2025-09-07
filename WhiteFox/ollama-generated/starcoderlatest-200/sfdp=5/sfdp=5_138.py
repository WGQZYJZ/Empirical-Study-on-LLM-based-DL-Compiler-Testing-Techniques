
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_proj = torch.nn.Linear(10, 16)
        self.key_proj = torch.nn.Linear(48, 54)
 
    def forward(self, x1):
        q = self.query_proj(x1[:, 0:256])
        k = self.key_proj(x1[:, 256:])
        v = x1[:, 256:]

        attn_weight = torch.softmax((q @ k.transpose(-2, -1)) / math.sqrt(k.size(-1)), dim=-1) # Scale the dot product of the query and key by sqrt(key size), apply softmax to this scaled dot product
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = (attn_weight @ v).sum(-2)

        return output


# Initializing the model
m = Model2()

 # Inputs to the model
x1 = torch.randn(10, 32, 768, 45)
