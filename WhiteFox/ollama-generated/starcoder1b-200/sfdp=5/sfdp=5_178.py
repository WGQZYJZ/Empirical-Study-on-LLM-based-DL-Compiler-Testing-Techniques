
class Model(torch.nn.Module):
    def __init__(self, attn_mask=None):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
        if attn_mask is not None:
            self.attn_mask = attn_mask
 
    def forward(self, x1):
        v1 = self.conv1(x1)
 
        if self.attn_mask is not None:
            qk  = x1 @ x1.transpose(-2, -1) / math.sqrt(v1.size(-1))
            attn_weight  = torch.softmax(qk, dim=-1)
            attn_weight  = torch.dropout(attn_weight, dropout_p, True)
            output  = attn_weight @ x1
        return output


# Initializing the model
m = Model()

