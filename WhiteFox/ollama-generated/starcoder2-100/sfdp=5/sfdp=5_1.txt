
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.scale = math.sqrt(query.size(-1))
 
    def forward(self, query, key, value):
        kq_dot = (query @ key.transpose(-2, -1)) / scale 
        kq_dot = kq_dot + attn_mask  
        softmax = torch.softmax(kq_dot, dim=-1)
        attn_weight = torch.dropout(softmax, dropout_p=0.5, inplace=True)
        output  = attn_weight @ value
        return output
