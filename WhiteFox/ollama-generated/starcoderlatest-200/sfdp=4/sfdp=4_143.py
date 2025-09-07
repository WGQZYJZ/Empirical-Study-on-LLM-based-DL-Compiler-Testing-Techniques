
 # Initializing the model
model = MultiHeadAttention()

 # Inputs to the model
q  = torch.randn(4, 3, 64, 64)
k = torch.randn(4, 8, 64, 64)
v = torch.randn(4, 128, 64, 64)

 # Attention computation: scaled dot product of v and attention weights
# Note that there is one extra axis with shape [bsz, n_head]. This is because we do 
#   qkv = q @ k. (v5+1)/).to(v3 +1)+).).).).to an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an an
