
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, query, key, value):
        attn_output, _ = self.attn(query, key, value)
        dropout_attn_output = torch.nn.functional.dropout(attn_output, p=dropout_p)
        output = dropout_attn_output + attn_output
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
