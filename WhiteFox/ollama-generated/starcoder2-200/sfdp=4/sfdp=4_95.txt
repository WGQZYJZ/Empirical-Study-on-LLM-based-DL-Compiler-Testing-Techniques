
class TransformerModel(torch.nn.Module):
    def __init__(self, d_model=512, num_heads=8, dff=None, dropout=0., query_dim=-1) -> None:
        super().__init__()
        self.d_model = d_model
        self.num_heads = num_heads
        self.dropout = torch.nn.Dropout(dropout)
 
    def forward(self, input):
        v0  = torch.split(input, self.d_model // 4 * (self.num_heads + 1), dim=2)
        v756 = self.linear(v0[7] + v0[-3]) 
        v849 = self.linear(v0[8] - v0[4]) 
        v971 = torch.cat([v756, v0[0], v0[2], v849, v0[1], v0[3]], 2)
        v34  = self.dropout(self._split_heads(self._feed_forward(v971), self.num_heads)) # Dropout is applied to the output of the feed-forward network
        v865 = torch.cat([input, v0[5], v0[-2]], 2) 
        v34 += self.attn(v865 + v0[7] * 1., v865 - v0[9], v865, v0[10]) # A scaled dot-product attention mechanism is applied to the output of the feed-forward network
        return v34
 
    def _split_heads(self, x, num_heads): 
        batch = x.shape[0]
        head_size  = self.d_model // num_heads
        new_len = x.shape[-2] * x.shape[-1] // self.d_model
        return torch.reshape(torch.transpose(x.view(-1, num_heads, new_len), -3 + (-1 if query_dim == 0 else query_dim) + (query_dim + 1), -(num_heads + 2)), batch * new_len // head_size, num_heads * self.d_model // num_heads).contiguous()
 
    def _feed_forward(self, x): 
        return torch.relu(x @ self.weights0.transpose(-1, -2) + self.weights1 + self.weights2)


