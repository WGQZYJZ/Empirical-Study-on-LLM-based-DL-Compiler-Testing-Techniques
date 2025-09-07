
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=32, num_heads=4)
 
    def forward(self, x1, x2):
        qk  = self.attention(x1, x2, x2)[0]
        scaled_qk  = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(16, 32, 56, 56)
x2  = torch.randn(16, 32, 56, 56)
