
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_q = torch.nn.Linear(128, 128)
        self.attn = torch.nn.MultiheadAttention(embed_dim=128, num_heads=4, dropout=0.25)
 
    def forward(self, q1, k1, v1):
        q2 = self.linear_q(q1)  # Apply linear transformation to the query tensor
        attn_output, _ = self.attn(q2, k1, v1)  # Compute the attention output using multihead attention
        output = (attn_output + q1).relu_()  # Apply non-linearity
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 128)  # Query tensor
k1 = torch.randn(1, 4, 128)  # Key tensor
v1 = torch.randn(1, 4, 128)  # Value tensor
