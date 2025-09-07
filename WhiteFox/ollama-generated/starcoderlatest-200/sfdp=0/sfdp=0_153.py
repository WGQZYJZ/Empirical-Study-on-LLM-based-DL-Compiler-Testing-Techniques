
class Attention(torch.nn.Module):
    def __init__(self, dim=128, num_heads=4):
        super().__init__()
        self.num_heads = num_heads
        self.scale = torch.sqrt(dim)
 
    def forward(self, qkv):
        batch_size, num_heads, seq_length, head_dim = qkv.shape
 
        q, k, v = qkv.chunk(3, dim=1)
        q *= (head_dim ** -0.5)
        attention_weights = torch.matmul(q, k.transpose(-2, -1))
        attention_weights = attention_weights / self.scale
        if num_heads > 1:
            attention_weights = attention_weights.softmax(dim=-1)
        attention_weights = self._dropout(attention_weights)
 
        x = torch.matmul(attention_weights, v)
        return x
 
    def _dropout(self, attention_weights):
        # In PyTorch, some dropout layers have already been applied
        # to q and k in the forward function, so we just need to apply them
        # once again here. If not, it can also help stabilize the gradients.
        attention_probs = torch.nn.functional.dropout(attention_weights, p=0.1, training=self.training)
        return attention_probs


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 256)
        self.dropout1 = torch.nn.Dropout()
        self.attention = Attention()
 
    def forward(self, x):
        y = self.linear(x)
        y = F.gelu(y)
        y = self.dropout1(y)
        # In PyTorch, some dropout layers have already been applied
        # to q and k in the forward function, so we just need to apply them
        # once again here. If not, it can also help stabilize the gradients.
        v = self.attention(self._qkv_reshape(q, k, v))
        x = torch.matmul(v, y)
        return x
 
    def _qkv_reshape(self, q, k, v):
        # Shape: [batch_size, num_heads, seq_length, head_dim]
        batch_size = q.shape[0]
        num_heads = self.num_heads
        seq_length = q.shape[1]
        head_dim = q.shape[-1]
 
        q = rearrange(q, "b n (n d) -> b n d", n=num_heads)
        k = rearrange(k, "b m (m d) -> b m d", m=num_heads)
        v = rearrange(v, "b o (o d) -> b o d", o=num_heads)
 
        qkv = torch.matmul(q, k.transpose(-2, -1)) * self.scale
        qkv = rearrange(qkv, "b n m d -> b n (m d)")
        qkv = torch.nn.functional.dropout(qkv, p=0.1, training=self.training)
 
        return qkv

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(256, 512, 4, 384, device="cuda")
