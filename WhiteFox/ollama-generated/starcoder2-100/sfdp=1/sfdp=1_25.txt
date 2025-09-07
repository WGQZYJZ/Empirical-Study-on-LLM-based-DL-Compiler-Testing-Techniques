
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk  = torch.nn.Linear(768, 768)

    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2,-1))
        v2  = v1.div(inv_scale_factor)
        v3  = v2.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=dropout_p) # dropout
        