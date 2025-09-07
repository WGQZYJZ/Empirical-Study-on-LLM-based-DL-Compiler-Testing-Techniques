
class MultiHeadAttnMultiHeadedModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.conv = torch.nn.Conv2d(3, 8, 1)
 
        self.layer_norm = torch.nn.LayerNorm((64))
        self.fc = torch.nn.Linear(64 * 4 * 4, 100)
 
    def forward(self, x):
        q = self.conv(x).view(-1, 8, 4, 4).transpose(-1, -2)
        k = self.conv(x).view(-1, 8, 4, 4).transpose(-1, -2)
        v = self.conv(x).view(-1, 8, 4, 4)
 
        q_norm = self.layer_norm(q.contiguous().view(-1, 64 * 4 * 4))

        attn_weights = (torch.einsum('...nd,...nk->...ni', q_norm, k.transpose(-2, -1))) / math.sqrt(
            query.size(-1))
        attn_weights += attn_mask
 
        attn_weights = torch.softmax(attn_weights, dim=-1)
        attn_weights = torch.dropout(attn_weights, dropout_p, True).contiguous()

        v_norm = self.layer_norm(v.transpose(-1, -2).contiguous().view(-1, 64 * 4 * 4))
        output = (torch.einsum('...ni,...nk->...nd', attn_weights, v_norm)).contiguous().view(x.size()[0], -1)
 
        return self.fc(output), q, k, v
 

# Initializing the model
m = MultiHeadAttnMultiHeadedModel()
 
# Inputs to the model
__input__ = torch.randn(4, 3, 64, 64).contiguous().view(-1, 3, 64, 64)
__output__, q, k, v = m(__input__)


