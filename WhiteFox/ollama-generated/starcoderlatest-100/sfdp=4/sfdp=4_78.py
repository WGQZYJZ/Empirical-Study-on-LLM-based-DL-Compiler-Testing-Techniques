qk = self.attn(x, k, v, attn_mask)[0]
output = torch.sum(qk, dim=-2)  # Reduce sum along last dimension
return output
