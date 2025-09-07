
class SelfAttention(torch.nn.Module):
    def __init__(self, d_model: int = 768, d_head: int = 128) -> None:
        super().__init__()
 
        self.d_model = d_model
        self.d_head = d_head
        self.qkv = torch.nn.Linear(in_features=self.d_model, out_features=(3 * d_head), bias=False)
 
    def forward(self, x):
        q, k, v  = self._split_heads(x)
 
        scale = math.sqrt(k.size(-1))
        attn_mask = torch.nn.ZeroPad2d((0, 0, 0, (q.size(2)*v.size(2)-k.size(3))))
        q = self._scaled_dot(q / scale) + attn_mask
 
        weight = torch.softmax(q, dim=-1).transpose(-2,-3)
        v = k@weight
 
        return self._reshape_back(v)
 
    @staticmethod
    def _split_heads(x):
        return torch.nn.functional.unfold(x,(self.d_head, 1), dilation=0, padding=0).permute([0,2,3,1]).contiguous().view(-1, *x.shape[-2:])
 
    @staticmethod
    def _scaled_dot(q):
        return torch.einsum('bijh,bihj->bihi', q)
 
    @staticmethod
    def _reshape_back(x):
        return x.permute([0, 3, 1, 2]).contiguous().view(-1,*x.shape[-2:])


# Initializing the model
model = SelfAttention()

