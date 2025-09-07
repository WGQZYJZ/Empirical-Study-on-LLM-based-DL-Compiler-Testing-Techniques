
class Model(torch.nn.Module):
    def __init__(self, args):
        super().__init__()
 
        self.attention = torch.nn.MultiheadAttention(args.hidden_size, 4)
        self.linear = torch.nn.Linear(args.hidden_size, args.vocab_size)
 
    def forward(self, x1, x2):
        qk = self.attention(x1, x2, x2)  # Compute the scaled dot product of x1 and x2
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, args.dropout_p, True)  # Apply dropout to the softmax output
        v = self.linear(attn_weight @ x2)  # Compute the dot product of the dropout output and the value
        return v


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
