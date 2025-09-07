
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        query = torch.randn((1, 512), device='cuda')
        key = torch.randn((1, 512), device='cuda')
        attn_mask = query.new_zeros(query.size()).byte()

        # Compute the dot product of the query and key, and scale it
        query = query @ key / math.sqrt(query.size(-1))
        query = query + attn_mask

        # Apply softmax to the result
        attn_weight = torch.softmax(query, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)

        value = torch.randn((1, 512), device='cuda')
        output = attn_weight @ value

        return output


# Initializing the model
m = Model()


