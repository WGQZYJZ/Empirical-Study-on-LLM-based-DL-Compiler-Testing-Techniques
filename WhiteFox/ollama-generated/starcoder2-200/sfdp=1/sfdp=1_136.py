class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):
        scale = torch.nn.functional.normalize(key)
        v1  = torch.matmul(query, scale.transpose(-2,-1))
        v2  = v1 / inv_scale_factor
        v3  = torch.nn.functional.softmax(v2, dim=-1)
        v4  = dropout(v3) #dropout is a function that returns dropout_qk above
        return v4 @ value
