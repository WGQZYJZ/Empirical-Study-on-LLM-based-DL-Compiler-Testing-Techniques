
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, h):
        super().__init__()
        self.W = torch.nn.Parameter(
            torch.zeros([h * 3])
            .view(
                [
                    h,
                    3,
                ]
            )
        )
 
    def forward(self, query, key, value, dropout_p=0.1):
        # Compute the dot product of the query and key
        output = torch.bmm(query, key.transpose(-2, -1))
 
        # Scale the dot product by 1/sqrt(h)
        scale = math.sqrt(self.W[-1].item())
        output /= scale
        output += self.W[0]
        attn_mask = self.W[3:6]
        for i in range(len(attn_mask)):
            output[:, :, :, 2, :output.size(-4) + 1 - i] -= \
                torch.diag(torch.ones(output.size(-4) + 1 - i)) * attn_mask[i].item()
 
        # Add the attention mask
        output += self._attn_mask
 
     