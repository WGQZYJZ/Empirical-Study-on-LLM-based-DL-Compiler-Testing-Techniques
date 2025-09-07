
class Attention(torch.nn.Module):
    def __init__(self, d_model, num_heads=8, dropout=0.1):
        super().__init__()
 
        self.num_heads = num_heads
        self.scale = 1 / (d_model ** (1/4))

        self.dropout = torch.nn.Dropout(p=dropout)

        self.q_layer_norm = torch.nn.LayerNorm(normalized_shape=[d_model], eps=1e-6, elementwise_affine=True)
        self.k_layer_norm = torch.nn.LayerNorm(normalized_shape=[d_model], eps=1e-6, elementwise_affine=True)

        self.q = torch.nn.Linear(in_features=d_model, out_features=d_model, bias=False)
        self.k = torch.nn.Linear(in_features=d_model, out_features=d_model, bias=False)
        self.v = torch.nn.Linear(in_features=d_model, out_features=d_model, bias=False)

    def forward(self, query, key, value, mask):
        nq, nx1, ni, nx2 = query.size()
        nh = self.num_heads

        d_k = query.view(nq, -1, nh).permute([0, 2, 1, 3]).contiguous().view(nq * nh, -1, ni)
        d_k = self.k(d_k).view(nq * nh, -1, nx2)

        d_v = value.view(nq, -1, nh).permute([0, 2, 1, 3]).contiguous().view(nq * nh, -1, ni)
        d_v = self.v(d_v).view(nq * nh, -1, nx2)

        scaled_qk = torch.einsum("...j,...jk->...ij", query, key).mul_(self.scale)

        qk = torch.einsum("...i,...jk->...ik", scaled_qk, d_k)
        qk = qk.view(nq, nh, -1, ni).permute([0, 2, 1, 3]).contiguous().view(nq, -1, nh, nx2)

        if mask is not None:
            masked_keys_indices = (key != torch.Tensor([]).to(mask.device)).nonzero()
            if len(masked_keys_indices[0]) > 0:
                qk = qk * (1 - mask[:, masked_keys_indices[0]].unsqueeze(-1)) + \
                     mask[:, masked_keys_indices[0]].unsqueeze(-1)

        qk = self.q_layer_norm(qk + query).view(nq, nh, nx2)
        attn_out = torch.nn.functional.dropout(qk, p=self.dropout, training=self.training)

        out = torch.einsum("...i,...ik->...j", attn_out, d_v)
        out = out.view(nq, nh, -1, nx2).permute([0, 2, 1, 3]).contiguous().view(nq, -1, ni)

        return out
