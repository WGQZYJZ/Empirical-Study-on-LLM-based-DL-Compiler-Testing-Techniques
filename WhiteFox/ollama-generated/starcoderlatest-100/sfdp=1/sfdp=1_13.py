
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(1, 8)
 
    def forward(self, query, key, value, scale_factor, dropout_p=0.5):
        scaled_qk = self.attention(query, key, value, scale_factor)[0]
        softmax_qk = scaled_qk.softmax(dim=-1)
        output = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2, 3, 64, 64)
