
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_query = torch.nn.Linear(1024, 512)
        self.attn_key   = torch.nn.Linear(1024, 512)
        self.attn_value = torch.nn.Linear(1024, 512)
 
    def forward(self, qk):
        attn_query = self.attn_query(qk).transpose(-2, -1) # transpose the first two dimensions of qk and apply linear transformation
        attn_key   = self.attn_key(qk)
        attn_value = self.attn_value(qk)

        attn_weight  = torch.softmax(attn_query @ attn_key / math.sqrt(1024), dim=-1) # apply softmax to the result and transpose back two dimensions of qk
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output  = attn_weight @ attn_value

        return output

# Initializing the model
m = Model()

# Inputs to the model
qk = torch.randn(1, 8, 64, 512)
