
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.math.sqrt(3072)
        self.attn = torch.nn.MultiheadAttention(embed_dim=3072, num_heads=48, dropout=0.1)
 
    def forward(self, x):
        q  = torch.randn(5, 6, 96, 96) # Create a random query tensor
        k = self.scale * q @ q.transpose(-3, -2).reshape(x.size())
        attn_mask = torch.zeros(k.shape[-1], k.shape[2], device=torch.device('cuda'), requires_grad=True)
        attn_mask  += (attn_mask > 0).nonzero()
        value = self.__output__
        attn_mask[:, :, attn_mask.size(-2):attn_mask.size(1)] -= float("inf") 
        v2, attn_weights = self.attn(query=q, key=k, value=value)
        v3  = torch.sum(torch.softmax(attn_weights + attn_mask), -1) @ value
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(5, 96*96, 48).view(5, 6, 96, 96) # Create a random input tensor for the model
__output__  = m(x)

