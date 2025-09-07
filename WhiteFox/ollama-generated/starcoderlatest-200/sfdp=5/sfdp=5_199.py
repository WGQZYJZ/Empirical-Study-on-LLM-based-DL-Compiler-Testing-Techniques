
class SelfAttention(torch.nn.Module):
    def __init__(self, dim_hidden: int = None, dropout_p: float = 0.1):
        super().__init__()
        if not dim_hidden:
            raise ValueError("`dim_hidden` should be a positive integer")
 
        self.attn_mask = torch.nn.Parameter(torch.zeros((1, 1, 64, 64)))
 
        self.query_conv = torch.nn.Conv2d(
            3, dim_hidden // 8 * 2, kernel_size=1, stride=1, padding=0
        )
        self.key_conv = torch.nn.Conv2d(
            3, dim_hidden // 8 * 2, kernel_size=1, stride=1, padding=0
        )
        self.value_conv = torch.nn.Conv2d(
            3, dim_hidden // 8 * 2, kernel_size=1, stride=1, padding=0
        )
 
        self.output_conv = torch.nn.Conv2d(
            dim_hidden // 8 * 2, 3, kernel_size=1, stride=1, padding=0
        )
 
        self.drop = torch.nn.Dropout2d(p=dropout_p)
 
    def forward(self, x):
        bs, c, h, w = x.shape
        q = torch.reshape(
            self.query_conv(x), (bs, 3 * dim_hidden // 8, h, w)
        ).permute(0, 2, 1, 3).contiguous()
 
        k = torch.reshape(
            self.key_conv(x), (bs, 3 * dim_hidden // 8, h, w)
        ).permute(0, 2, 1, 3).contiguous()
 
        v = torch.reshape(
            self.value_conv(x), (bs, 3 * dim_hidden // 8, h, w)
        ).permute(0, 2, 1, 3).contiguous()
 
        qk = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
 
        output = self.drop(attn_weight) @ v.permute(0, 2, 1, 3).contiguous()
 
        output = torch.reshape(
            self.output_conv(output), (bs, 3, h, w)
        )
 
        return output


# Model instance
attention = SelfAttention(dim_hidden=512)
 
def attention_module(self, x):
    