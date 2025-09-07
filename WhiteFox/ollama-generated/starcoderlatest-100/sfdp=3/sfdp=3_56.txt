
class Model(torch.nn.Module):
    def __init__(self, n_head=8, n_layers=1, hidden_size=128):
        super().__init__()
 
        self.n_head = n_head
        self.d_key = self.n_head * hidden_size
        self.d_value = self.n_head * hidden_size
        self.d_model = self.d_key + self.d_value
 
        # This block configures the query, key and value linear projection matrices
        self.linear_q = torch.nn.Linear(self.d_model, self.d_key)
        self.linear_k = torch.nn.Linear(self.d_model, self.d_key)
        self.linear_v = torch.nn.Linear(self.d_model, self.d_value)
 
        # This block applies a multi-head attention mechanism to the query and key tensors with the same number of heads (8 in this case)
        self.attn = torch.nn.MultiheadAttention(
            num_heads=self.n_head,
            input_dim=self.d_key,
            output_dim=self.d_value)
 
        # This block computes the outputs of the scaled dot product and softmax function, then applies dropout to each result
        self.linear_out = torch.nn.Linear(self.d_model, 2 * self.n_head * hidden_size)
 
    def forward(self, x):
        q = self.linear_q(x).permute([0, 2, 1, 3]) # (batch size, time length, query length, head dim)
        k = self.linear_k(x).permute([0, 2, 3, 1]) # (batch size, memory length, key length, head dim)
        v = self.linear_v(x)
 
        x1, attn_weights = self.attn(q, k, v) # (batch size, query length, key length, hidden dim)
        x2 = torch.tanh(self.linear_out(torch.cat([x1, x], dim=1))).permute([0, 3, 1, 2])
        return x2
 
