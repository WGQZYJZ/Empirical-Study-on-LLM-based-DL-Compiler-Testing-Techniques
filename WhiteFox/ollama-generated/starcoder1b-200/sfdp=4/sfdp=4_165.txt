
class Model(torch.nn.Module):
    def __init__(self, dim1, dim2):
        super().__init__()
        self.dim1 = dim1
        self.dim2 = dim2

    def forward(self, x1, x2):
        if x1.shape[-1] != x2.shape[-1]:
            raise RuntimeError('the dimension of the query and key should be the same')

        # [batch size, max_length, feature dim 1] -> [batch size, max_length, feature dim 2]
        x1 = torch.transpose(x1, 0, 1) # [batch size, feature dim 1, max_length]
        x2 = torch.transpose(x2, 0, 1)

        # [batch size, feature dim 1, max_length] -> [batch size, max_length, feature dim 2]
        x1 = x1.view(-1, self.dim1, -1) # [batch size * max_length, feature dim 1]
        x2 = x2.view(-1, self.dim2, -1) # [batch size * max_length, feature dim 2]

        k = x1 @ x2  # [batch size * max_length, batch size * max_length, feature dim 1, feature dim 2]
        v = x2 @ x2  # [batch size * max_length, batch size * max_length, feature dim 2, feature dim 2]

        # [batch size * max_length, batch size * max_length, feature dim 1, feature dim 2] -> [batch size * max_length, batch size * max_length, feature dim 2, feature dim 2]
        k = k.view(-1, x1.shape[-1], -1)
        v = v.view(-1, x2.shape[-1], -1)

        # [batch size * max_length, batch size * max_length, feature dim 1, feature dim 2] / sqrt(feature dim 1) -> [batch size * max_length, batch size * max_length, feature dim 1, feature dim 1]
        k = torch.div(k, math.sqrt(x1.shape[-1]))

        # [batch size * max_length, batch size * max_length, feature dim 1, feature dim 2] / sqrt(feature dim 2) -> [batch size * max_length, batch size * max_length, feature dim 2, feature dim 2]
        v = torch.div(v, math.sqrt(x2.shape[-1]))

        # [batch size * max_length, batch size * max_length, feature dim 1, feature dim 2] + 1 -> [batch size * max_length, batch size * max_length, feature dim 2, feature dim 2]
        attn = k + 1 - torch.abs(v) # [batch size * max_length, batch size * max_length, feature dim 2, feature dim 2]

        # Apply softmax to the result
        attn_weight = torch.softmax(attn, dim=-1) # [batch size * max_length, batch size * max_length, feature dim 2, feature dim 2]

        # [batch size * max_length, batch size * max_length, feature dim 1, feature dim 2] @ [batch size * max_length, batch size * max_length, feature dim 2, feature dim 2] -> [batch size * max_length, batch size * max_length, feature dim 2, feature dim 2]
        output = attn_weight @ value # [batch size * max_length, batch size * max_length, feature dim 1, feature dim 2] @ [batch size * max_length, batch size * max_length, feature dim 2, feature dim 2] -> [batch size * max_length, batch size * max_length, feature dim 1, feature dim 2]

        return output


# Initializing the model
m = Model(8, 16)
x1 = torch.randn(1, 8, 64, 64)
