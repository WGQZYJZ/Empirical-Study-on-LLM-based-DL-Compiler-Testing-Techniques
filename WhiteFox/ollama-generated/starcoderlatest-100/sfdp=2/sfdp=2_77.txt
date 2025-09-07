
class MultiHeadSelfAttention(torch.nn.Module):
    def __init__(self, n_heads, head_dim):
        super().__init__()
        self.n_heads = n_heads
        self.head_dim = head_dim
        assert head_dim % n_heads == 0, f"Error: The dimension of head should be a multiple of the number of heads."
        self.w_q = torch.nn.Linear(self.n_heads*self.head_dim, self.n_heads * self.head_dim)
        self.w_k = torch.nn.Linear(self.n_heads*self.head_dim, self.n_heads * self.head_dim)
        self.w_v = torch.nn.Linear(self.n_heads*self.head_dim, self.n_heads * self.head_dim)
 
    def forward(self, x):
        bs, c, h, w = x.shape

        x = x.reshape(bs, c, -1) # [batch, channel, head_dim] -> (batch, head_dim, width*height)
        qk = torch.split(x, self.n_heads * self.head_dim, dim=1) # Split the tensor into n heads
        q, k, v = [qk[i].reshape(bs, self.n_heads, -1) for i in range(3)] # Reassemble tensors

        wq = self.w_q(torch.flatten(q, 2)).reshape(-1, bs, self.n_heads, self.head_dim)
        vk = self.w_k(torch.flatten(k, 2)).reshape(-1, bs, self.n_heads, self.head_dim)
        vv = self.w_v(torch.flatten(v, 2)).reshape(-1, bs, self.n_heads, self.head_dim)

        wq = torch.transpose(wq, -2, -3).contiguous() # [batch, head, height*width, head_dim] -> (batch, head_dim, height*width, head)
        vk = torch.transpose(vk, -2, -3).contiguous()
        vv = torch.transpose(vv, -2, -3).contiguous()
 
        out = wq + vk  # Add the outputs of queries and keys using attention mechanism
        out = torch.nn.functional.relu(out)

        out = self.dropout_apply(out, dropout_p) # Apply dropout to output
        out = out @ vv # Compute the dot product between output and values
 
        return torch.transpose(out, -2, -3).contiguous().view(bs, -1, h, w)  # Reassemble outputs and reshape
 
    def dropout_apply(self, x, p):
        