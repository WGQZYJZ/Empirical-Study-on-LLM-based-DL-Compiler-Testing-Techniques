
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask=None, value=None):
        qk = torch.einsum('bij,bik->bkij', query, key) / math.sqrt(query.size(-1))  # compute the dot product of query and key
        if attn_mask is not None:
            qk += attn_mask  # add the attention mask to the scaled dot-product
        attn_weight = torch.softmax(qk, dim=-2)  # apply softmax on the result
        output = (attn_weight @ value).transpose(-1, -2)  # compute the dot product of the attn weights and value tensor
        return output


m = MyModel()


query = torch.randn(3, 50, 4096)
key = query + torch.randn(3, 50, 4096)
 
output = m(query, key)
