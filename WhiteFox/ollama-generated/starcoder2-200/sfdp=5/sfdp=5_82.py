
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: Tensor = None) -> Tensor:  # Input Tensor
        qk = torch.bmm(query, query[None, :, :].transpose(-2, -1)) / math.sqrt(query.size(-1))
        qk = qk + attn_mask[:, None, :]
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output  = attn_weight @ value
        return output


# Initializing the model