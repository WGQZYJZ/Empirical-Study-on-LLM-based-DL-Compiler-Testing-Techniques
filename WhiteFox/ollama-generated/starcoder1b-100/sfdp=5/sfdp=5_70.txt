
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        k1 = torch.einsum("b c d, b c h -> bc h", x1, x2)
        k1 /= math.sqrt((k1 ** 2).sum(dim=-1, keepdim=True))
        attn_mask = torch.eye(x2.shape[0], device=k1.device)[None] + (torch.rand(attn_mask.size()[0]).to(attn_mask.device) > 0.5).unsqueeze(-1)

        k1 = k1 * attn_mask
        k1  = torch.softmax(k1, dim=-1)
        output = k1 @ x2
        return output


# Initializing the model
m = Model()

