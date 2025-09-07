
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.attn_conv(x1)
        v2 = self.attn_conv(x2)
        attn_weight = torch.softmax(v1 @ v2, dim=-1)  # [B, L_s, H, W] -> [B, L_q, L_k]
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = attn_weight @ v1  # [B, L_q, H, W] -> [B, L_s, H, W]

        return output


# Initializing the model
m = Model()


