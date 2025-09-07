
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v, attn_mask=None):
        b, nq = q.size()[:2]
        b, _, nd  = k.size()[:3]
 
        scale  = torch.rsqrt(torch.tensor([nd]))
        
        attn_score  = q @ k.transpose(-1, -2) * scale
        if attn_mask is not None:
            attn_score += attn_mask 
        attn_weight  = F.softmax(attn_score, dim=-1)
        
        output  = torch.einsum('bln, blkd -> blnk', attn_weight, v)
        return output
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.attn  = ScaledDotProductAttention()
 
        # This mask is used to prevent attention to the positions after the padding position of the source tensor
        attn_mask  = torch.ones([1, k.size(-2), k.size(-1)]).bool().to(k)
        attn_mask[:, :, q.size(-1):] = False

        # Generate query, key, and value tensors by performing convolutions on the input tensor
        self.convq  = torch.nn.Conv2d(8, 304, kernel_size=7, stride=1)
        self.convk  = torch.nn.Conv2d(56, 392, kernel_size=7, stride=1)
        self.convv  = torch.nn.Conv2d(80, 488, kernel_size=7, stride=1)
 
        # Generate a query tensor
        vq = torch.randn([b, nq, 304])

        # Generate a key and value tensor from the input tensor using convolutions
        k = self.convk(x1).permute((0, 2, 1)).contiguous()
        v = self.convv(x1)
 
        # Compute attention with mask
        __output__  = self.attn(vq, k, v, attn_mask=attn_mask)

# Initializing the model
m = Model()

