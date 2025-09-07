
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, input_dim, num_heads=8):
        super().__init__()
        self.num_heads = num_heads # number of heads
        self.q_linear = nn.Linear(input_dim, input_dim)
        self.k_linear = nn.Linear(input_dim, input_dim)
        self.v_linear = nn.Linear(input_dim, input_dim)
        self.output_linear = nn.Linear(input_dim, input_dim)
 
    def forward(self, x):
        q1 = self.q_linear(x).unsqueeze(-1)  # (batch_size, seq_len, head_size, 1) 
        k1 = self.k_linear(x).transpose(-2, -1).unsqueeze(-2)  # (batch_size, seq_len, head_size, head_dim) 
        v1 = self.v_linear(x).transpose(-2, -1)  # (batch_size, seq_len, head_size, head_dim) 
        q2 = torch.einsum('bshd,bhd->bshd', [q1, k1])  # (batch_size, seq_len, head_size, seq_len) 
        softmax_qk = nn.functional.softmax(q2, dim=-1)
        dropout_qk = nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output1 = torch.einsum('bshd,bsd->bshd', [dropout_qk, v1])  # (batch_size, seq_len, head_size, head_dim) 
        # This is what we use to implement multi-head attention in PyTorch
        # Please don't get confused by the function name.

        output2 = self.output_linear(output1).squeeze(-1)  # (batch_size, seq_len, input_dim) 
        return output2

# Inputs for the model
x = torch.randn(1, 8, 32, 64)
mha = MultiHeadAttention(input_dim=64)
