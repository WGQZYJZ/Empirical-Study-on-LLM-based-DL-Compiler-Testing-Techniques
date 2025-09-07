
class AttentionLayer(torch.nn.Module):
    def __init__(self, d_model, dropout=0.1):
        super().__init__()
        self.attn_layer = torch.nn.Linear(d_model, d_model)
        self.drop_out = torch.nn.Dropout(dropout)
 
    def forward(self, query, key, value):
        k_shape = key.size()[:-1] + (query.size(-2), query.size(-1))
        qk_t = torch.matmul(query, self.attn_layer(key).transpose(-2, -1)) / math.sqrt(q_head * k_head)
        qk_t = self.drop_out(qk_t)
        attn_weight = torch.softmax(qk_t, dim=-1)
        attn_output = torch.matmul(attn_weight, value).transpose(-2, -1)
        return attn_output, attn_weight

class AttentionNet(torch.nn.Module):
    def __init__(self):
        super().__init__()
        d_model = 512
        self.key = torch.nn.Linear(d_model, d_model * 2)
        self.query = torch.nn.Linear(d_model, d_model * 2)
 
        self.value = torch.nn.Linear(d_model, d_model * 4)
        self.attn_layer = AttentionLayer(d_model)
 
    def forward(self, x1):
        qk_output, attn_weight = self.attn_layer(x1, self.query(x1), self.value(x1))
 
        return (qk_output + x1).view(-1, d_model), attn_weight

# Initializing the model
a_net = AttentionNet()


# Inputs to the model
x1 = torch.randn(64, 512, 64, 64)
__output__, __attn_weight__ = a_net(x1)


