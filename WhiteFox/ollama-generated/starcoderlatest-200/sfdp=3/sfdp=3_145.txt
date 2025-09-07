
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_module = torch.nn.MultiheadAttention(num_heads=1, kdim=None, vdim=64)
 
    def forward(self, x, y):
        a1, attn_output1 = self.attention_module(x, x, x, mask_value=-1000.0) # Mask the attention output of the input to -1000 by default (not necessary)
        a2, _  = self.attention_module(a1, y, y, mask_value=0.)
        attn_output2 = torch.nn.functional.relu(attn_output1) * 10 + 10
        return attn_output2
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 8, 64, 64).permute(1, 0, 2, 3) # (b x n x h x w), b: batch size, n: number of heads, h and w are height and width of each head
y1 = torch.randn(2, 8, 12, 64).permute(1, 0, 2, 3) # (b x m x o x h), b: batch size, m: number of heads, o is output feature dimension, h is height and width of each head
