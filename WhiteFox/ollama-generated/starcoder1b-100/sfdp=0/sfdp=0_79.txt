
class Model(torch.nn.Module):
    def __init__(self, num_heads=8):
        super().__init__()
        self.num_heads = num_heads
        self.scale = 1 / math.sqrt(num_heads)
 
        self.qkv = torch.nn.Linear(2048, 36 * 3 * 8)
        self.layernorm1 = LayerNorm(2048)
        self.layer_norm2 = LayerNorm(2048)
 
    def forward(self, x):
        # Batch size is 1 for the Transformer-XL architecture, 
        # and can be set to any other value with x.shape[0] % num_heads == 0
        batch_size = int(x.shape[0]) // self.num_heads
        qkv = self.qkv(x).chunk(3, dim=2)  # Split the input tensor into head_size * batch_size parts, where 
        # 36 is num_heads, and then reshape them to heads * batch_size * hidden_dim
        q = qkv[0].reshape(-1, self.num_heads, batch_size, -1)  # Unfold the result into the batch dimension
        k = qkv[1].reshape(-1, self.num_heads, batch_size, -1) 
        v = qkv[2].reshape(-1, self.num_heads, batch_size, -1)
 
        # Scale the input and perform softmax to compute attention weights
        x_scale = torch.tensor(self.scale).to(x.device)  # The square root of dimension of key vectors
        q *= x_scale
        k *= x_scale
        v *= x_scale
        attention_weights = torch.softmax(q, dim=-1)
        scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) / x_scale
 
        # Concatenate the query and key vectors and perform layer normalization
        x = torch.cat([q, v], dim=0)  # The concatenation is the same for all heads
        x += self.layernorm1(x)
        x *= self.scale  # The scale factor is 1/sqrt(num_heads) because the batch size of input and output are 
        # not necessarily divisible by num_heads, and they are both set to 1 for Transformer-XL
        
        # Perform elementwise multiplcation on the input tensor and the attention weights
        # Then compute the output with layer norm
        x = torch.einsum('bhjcd->bhc', [x, attention_weights])
        x += self.layer_norm2(x)
 
        return x


# Initializing the model
m = Model()


