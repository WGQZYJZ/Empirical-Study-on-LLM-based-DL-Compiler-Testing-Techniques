
class Model(torch.nn.Module):
    def __init__(self, num_heads=4):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
        self.output_layer  = torch.nn.Linear(num_heads * hidden_size, output_size)

    def forward(self, x1, x2, dropout_p=0.1):
        qk = self.attention(x1, x2, x2)
        scaled_qk = qk.div(torch.pow(self.attention.scale_factor, -1).unsqueeze(-2).expand_as(qks))
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=dropout_p)
        v = self.output_layer(dropout_qk)
        return v


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(batch_size, num_heads, hidden_size, 64)
x2 = torch.randn(batch_size, num_heads, hidden_size, 64)
