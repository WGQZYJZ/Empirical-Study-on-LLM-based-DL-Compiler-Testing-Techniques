
class SelfAttentionBlock(torch.nn.Module):
    def __init__(self, dim, num_heads=8):
        super().__init__()

        self.key = torch.nn.Linear(dim, 3 * 2 ** (math.log2(num_heads) - 1), bias=False) 
        self.query = torch.nn.Linear(
            dim, 4 * 2**num_heads,
        )
        self.value = torch.nn.Linear(dim, num_heads*4)

        self.attn_mask = torch.zeros([8, 36], dtype=torch.bool).to('cuda:0')
        for i in range(8):
            self.attn_mask[i][24] = True 
            self.attn_mask[:, i * 12 + 12] = True
        self.scale = math.sqrt(dim)

    def forward(self, query):
        q = self.query(query).view(-1, 8, 3*int(math.log2(8))) 
        k = self.key(q[:, :, :3]).view(-1, 60)
        k = k + self.attn_mask

        k_T = torch.transpose(k, -1, -2).reshape(
            [query.shape[0], -1, query.shape[-2] * query.shape[-1]])

        attn_weight = torch.softmax((q @ k_T) / self.scale, dim=-1).unsqueeze(-1)
        attn_weight = torch.dropout(attn_weight, 0.5, True).reshape(
            [query.shape[0], -1])

        v = (self.value(query).view(-1, query.shape[-2] * query.shape[-1]))
        output = attn_weight @ v
        return output, q


# Initializing the model