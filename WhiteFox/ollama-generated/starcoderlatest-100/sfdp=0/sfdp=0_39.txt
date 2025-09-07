
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, q, k, v, inv_scale):
        v  # unused for this test
        scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        return attention_weights

class MultiHeadAttention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.norm  = torch.nn.LayerNorm(dim)
        self.attn_dropout = torch.nn.Dropout(0.5)
        self.attn = ScaledDotProductAttention(dim=dim)
 
    def forward(self, x1, x2):
        residual = x1 + x2
        x3 = self.norm(x1 + x2)  # Normalize the intermediate results for use in attention computation
        attn_weights = self.attn(q=x3, k=x3, v=x2, inv_scale=1 / x3.shape[-1])
        output = attn_weights.matmul(x2)
        return x3 + residual * (1 - attn_weights).permute(0, 2, 1) # Perform attention-based scalar multiplication

class EncoderLayer(torch.nn.Module):
    def __init__(self, dim, heads=8):
        super().__init__()
        self.norm_1 = torch.nn.LayerNorm(dim)
        self.attn_layer = MultiHeadAttention(dim=dim)
        self.norm_2 = torch.nn.LayerNorm(dim)
        self.ff_layer = torch.nn.Sequential(
            torch.nn.Linear(dim, dim * 4),
            torch.nn.ReLU(),
            torch.nn.Linear(dim * 4, dim),
            torch.nn.Dropout(0.25),
        )
 
    def forward(self, x1):
        residual = x1 + x1
        x3 = self.norm_1(x1)  # Normalize the intermediate results for use in attention computation
        attn_weights = self.attn_layer(q=x3, k=x3, v=x1, inv_scale=1 / x3.shape[-1])
        output = x3 + residual * (1 - attn_weights).permute(0, 2, 1) # Perform attention-based scalar multiplication
        x5 = self.norm_2(output)  # Normalize the intermediate results for use in feed-forward computation
        x6 = self.ff_layer(x5)
        return x3 + output * (1 - attn_weights).permute(0, 2, 1)  + residual * (1 - attn_weights).permute(0, 2, 1)

class Encoder(torch.nn.Module):
    def __init__(self, dim=512):
        super().__init__()
        self.layers = torch.nn.Sequential(*[EncoderLayer(dim, heads=8) for _ in range(6)])
 
    def forward(self, x1):
        return self.layers(x1).permute(0, 2, 1)

class DecoderLayer(torch.nn.Module):
    def __init__(self, dim, heads=8):
        super().__init__()
        self.norm_1 = torch.nn.LayerNorm(dim)
        self.attn_layer = MultiHeadAttention(dim=dim)
        self.norm_2 = torch.nn.LayerNorm(dim)
        self.ff_layer_1 = torch.nn.Sequential(
            torch.nn.Linear(dim, dim * 4),
            torch.nn.ReLU(),
            torch.nn.Linear(dim * 4, dim),
            torch.nn.Dropout(0.25),
        )
        self.norm_3 = torch.nn.LayerNorm(dim)
        self.ff_layer_2 = torch.nn.Sequential(
            torch.nn.Linear(dim, dim * 4),
            torch.nn.ReLU(),
            torch.nn.Linear(dim * 4, dim),
            torch.nn.Dropout(0.25),
        )
 
    def forward(self, x1, x2):
        residual = x2 + x1
        x3 = self.norm_1(x2)  # Normalize the intermediate results for use in attention computation
        attn_weights_1 = self.attn_layer(q=x3, k=x3, v=x2, inv_scale=1 / x3.shape[-1])
        output = x3 + residual * (1 - attn_weights_1).permute(0, 2, 1) # Perform attention-based scalar multiplication
        x5 = self.norm_2(output)  # Normalize the intermediate results for use in feed-forward computation
        x6 = self.ff_layer_1(x5)
        x7 = x6 + output * (1 - attn_weights_1).permute(0, 2, 1)
        x8 = residual * (1 - attn_weights_1).permute(0, 2, 1)
        output_2 = self.norm_3(x8) # Normalize the intermediate results for use in feed-forward computation
        x9 = self.ff_layer_2(output_2)
        return x8 + output * (1 - attn_weights_1).permute(0, 2, 1)  + x7 * (1 - attn_weights_1).perm2/lib
class Solution:
 


class Phrase:

    # def __init__(self, phrase: str):
    