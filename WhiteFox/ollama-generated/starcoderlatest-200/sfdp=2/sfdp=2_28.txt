
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_q = torch.nn.Linear(256, 512)
        self.attn_k = torch.nn.Linear(512, 256)
        self.attn_v = torch.nn.Linear(256, 256)
 
        self.ff_q = torch.nn.Linear(256, 512)
        self.ff_k = torch.nn.Linear(512, 256)
        self.ff_v = torch.nn.Linear(256, 256)
 
        self.proj = torch.nn.Linear(256, 384)
 
    def forward(self, x):
        x1 = self.attn_q(x) # Self-attention in the query dimension
        attn_qk = torch.softmax(x1, dim=-1) # Softmax operation for the dot product in the query dimension
        out_q = x * attn_qk  # Dot Product of the query and the attention scores
        x2 = self.attn_k(out_q) # Self-attention in the key dimension
        attn_kv = torch.softmax(x2, dim=-1) # Softmax operation for the dot product in the key dimension
        out_v = out_q * attn_kv  # Dot Product of the attention scores and the keys
        x3 = self.attn_v(out_v) # Self-attention in the value dimension
 
        x4 = self.ff_q(x1) # Fully connected layer in the query dimension
        ff_qk = torch.tanh(self.ff_k(x4))  # Apply hyperbolic tangent to the result of the fully connected layer in the query dimension
        ff_qk2 = torch.softmax(ff_qk, dim=-1)  # Apply softmax operation to the output from the fully connected layer in the query dimension
        out_q = x3 * ff_qk2  # Dot Product between the output of the self-attention and the output of the fully connected layers in the query dimension
 
        x5 = self.ff_k(x4) # Fully connected layer in the key dimension
        ff_kv = torch.tanh(self.ff_v(x5))  # Apply hyperbolic tangent to the result of the fully connected layer in the key dimension
        ff_kv2 = torch.softmax(ff_kv, dim=-1)  # Softmax operation for the output from the fully connected layer in the key dimension
        out_v = x3 * ff_kv2  # Dot Product between the output of the self-attention and the output of the fully connected layers in the key dimension
 
        x6 = torch.tanh(self.proj(torch.cat((out_q, out_v), dim=-1)))  # Concatenate the outputs of the self-attention and the fully connected layers in the value dimension
        return x6


# Initializing the model
m = Model()
 
# Inputs to the model
x = torch.randn(1, 256, 7, 7)
