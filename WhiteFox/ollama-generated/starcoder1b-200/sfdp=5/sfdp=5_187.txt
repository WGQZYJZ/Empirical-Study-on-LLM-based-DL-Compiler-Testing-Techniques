
class Model(torch.nn.Module):
    def __init__(self, num_heads=2, hidden_dim=16):
        super().__init__()
        self.num_heads = num_heads
        self.hidden_dim = hidden_dim
        self.attention  = torch.nn.MultiheadAttention(
            input_dim=hidden_dim, 
            hidden_dim=self.hidden_dim * num_heads,
            num_heads=self.num_heads)
        self.feedforward  = torch.nn.Linear(input_dim=hidden_dim*2, output_dim=hidden_dim)
 
    def forward(self, x1):
        # Input: bsz, seq_len, hidden_dim
        h1 = self.attention(x1, x1, x1)  # q, k, v = B.H @ B.H. t1t1 and t2t2 are input tensors
        # Forward pass through the feedforward network to obtain output: bsz, seq_len, hidden_dim
        o1 = self.feedforward(h1 + h1)  # q + k
        return o1

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
