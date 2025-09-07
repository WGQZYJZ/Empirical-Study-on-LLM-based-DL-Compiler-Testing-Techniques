class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, attn_mask3, value4):
        v5 = torch.matmul(query1, torch.transpose(key2, -2, -1)) / math.sqrt(torch.size(-1))  # Compute the dot product of the query and key
        v7 = torch.add(v6, attn_mask3)
        v8  = torch.softmax(v5, dim=-1)  # Apply softmax to the result
        return torch.matmul(value4, v8)
