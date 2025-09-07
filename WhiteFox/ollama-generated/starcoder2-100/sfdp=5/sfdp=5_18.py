
class TransformerModel(torch.nn.Module):
    def __init__(self, config: Config):
        super().__init__()
 
        query = torch.rand(320, 192)
        key = torch.rand(384, 192)
        value = torch.rand(768, 192)
        attn_mask = torch.zeros((320, 384))
 
        v1 = query @ key.transpose(-2,-1)/math.sqrt(query.size(-1))
        v1 = v1 + attn_mask 
        v2 = torch.softmax(v1, dim=-1)
        v2 = torch.dropout(v2, dropout, True)
 
        v3  = v2 @ value
        __output__  = v3

    # Initializing the model
    m = TransformerModel(Config())

