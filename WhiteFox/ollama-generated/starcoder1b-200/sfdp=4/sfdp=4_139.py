
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = torch.zeros((3, 64, 64))  # Attention mask

        self.conv1 = nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = nn.Conv2d(8, 16, 1, stride=1, padding=0, bias=False)
        self.conv_ln = torch.nn.LayerNorm((16,), eps=1e-5)
        self.pool = nn.AvgPool2d((1, 4), stride=(3, 2))

        self.qkv = self._make_qkv()
 
    def _make_qkv(self):
        kdim = 16
        qdim = 64
        vdim = 64

        wdim = math.log(kdim / qdim) * math.pi
        return nn.Linear((qdim, ), (2 * wdim, ), bias=False), \
               nn.Linear((qdim, kdim // 8), (2 * wdim, ), bias=False), \
               nn.Linear((vdim, ), (wdim, ) + (kdim // 8,))
 
    def forward(self, x1, x2):
        # (B, C_in, H_in, W_in) -> (B, N * C_in // groups, D_in)

        B = x1.shape[0]
        G = math.log(x1.shape[-1]) / 64  # Grouping factor

        w = torch.zeros((2 * wdim,) + (kdim // 8,), device=x1.device)  # Initial weights for query, key and value
        self.attn_mask = torch.triu(torch.ones((3, ) + x1.shape[-2:], device=x1.device), 0).unsqueeze(-2)  # (1, 3, H_in, W_in)
        self.attn_mask *= (1 - self.attn_mask.diag())  # mask the diagonal elements with zeros

        q, k, v = self.qkv(x2)  # Compute query, key and value from (B, C, D_in)

        # (B, N * C // groups, H_in * W_in) -> (B, N * C // groups, D_in // G)
        x1 = self.pool(F.linear(x1, q, bias=None))  # (B, N * C // groups, H_in) -> (B, N * C // groups, D_in // G)
        # (B, N * C // groups, D_in // G) -> (B, N * C // groups, K * V // G)
        x1 = x1.reshape(B, G, -1).contiguous()  # (B, N * C // groups, K * V // G) -> (B, N * C // groups, D_in)

        # (B, N * C // groups, H_in * W_in) -> (B, N * C // groups, H_out)
        x2 = F.linear(x2, k, bias=None).reshape(B, G, -1).contiguous()  # (B, N * C // groups, K * V // G) -> (B, N * C // groups, H_in)
        x2 = self.pool(F.linear(x2, v, bias=None))  # (B, N * C // groups, D_in) -> (B, N * C // groups, H_out)

        x = torch.einsum('bgd,bhmd->bhi', x1, x2)  # Compute weighted sum of the tensors in x
        x = self.conv_ln(x + w).reshape(B, G, -1)  # Linear layer before normalization
        x = F.relu(self.conv1(x))

        return torch.einsum('bgi,bhmd->bhi', x, w), \
               self.attn_mask.unsqueeze(-2).repeat((1, G)).transpose(-1, -2)

    def forward_inference(self, x):
        w = self.qkv(x)[0]
        y  = torch.einsum('bgd,bhmd->bhi', x, w)
        return self.conv_ln(y + w), y
