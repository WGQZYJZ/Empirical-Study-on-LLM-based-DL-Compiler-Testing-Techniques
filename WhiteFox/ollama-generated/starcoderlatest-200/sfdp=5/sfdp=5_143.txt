
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 4)
 
    def forward(self, x1, x2):
        qk, _ = self.attn(x1, x2, x2)
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = attn_weight @ x2
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 4, 64, 64) # Batch size is set to 1 due to a single input
x2 = torch.randn(1, 8, 64, 64) # Number of heads should be different from previous models due to multihead attention layers
