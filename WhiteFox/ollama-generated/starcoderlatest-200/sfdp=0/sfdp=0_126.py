
class Attention(torch.nn.Module):
    def __init__(self, dim1, dim2=None, dropout=0.1):
        super().__init__()
        if not dim2:
            dim2 = dim1
        self.dim1 = dim1
        self.conv_q = torch.nn.Conv2d(dim1, dim2, 1, stride=1, padding=0)
        self.bn_q = torch.nn.BatchNorm2d(dim2)
        self.dropout = torch.nn.Dropout(p=dropout)
        self.conv_k = torch.nn.Conv2d(dim1, dim2, 1, stride=1, padding=0)
        self.bn_k = torch.nn.BatchNorm2d(dim2)
        self.conv_v = torch.nn.Conv2d(dim1, dim2, 1, stride=1, padding=0)
        self.bn_v = torch.nn.BatchNorm2d(dim2)
 
    def forward(self, x):
        n, c, h, w = x.shape
        q = self.conv_q(x).view(n, -1, c) # (N*H*W, C, d) --> (N, H, W, C, d)
        k = self.conv_k(x).view(n, -1, c) # (N*H*W, C, d) --> (N, H, W, C, d)
        v = self.conv_v(x).view(n, -1, c) # (N*H*W, C, d) --> (N, H, W, C, d)
 
        q = self.bn_q(q)
        k = self.bn_k(k)
        v = self.bn_v(v)
 
        attn_weights = torch.bmm(q, k.transpose(-2, -1))  # (N, H, W, d, d) @ (d, d, C*H*W) -> (N, H, W, d, d)
        attn_weights = attn_weights / math.sqrt(attn_weights.shape[-1])
 
        attn_weights = torch.softmax(attn_weights, dim=-1)
        attn_weights = self.dropout(attn_weights)
        output = torch.bmm(attn_weights, v)  # (N, H, W, d, C) --> (N, H*W, d, C)
 
        return output
 

class Model(torch.nn.Module):
    def __init__(self, dim1=256, nhead=8, dropout=0.1):
        super().__init__()
        self.attn = Attention(dim1, nhead, dropout)
 
    def forward(self, x):
        output = self.attn(x)
        return output
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 256, 10, 10)
