
class Model(torch.nn.Module):
    def __init__(self, num_attention_heads=8, input_size=(256, 3)):
        super().__init__()
        self.query = torch.nn.Linear(input_size[1],
                                        num_attention_heads * input_size[0])
        self.key = torch.nn.Linear(input_size[1],
                                    num_attention_heads * input_size[0])
        self.value = torch.nn.Linear(input_size[1],
                                     num_attention_heads * input_size[0])

    def forward(self, x):
        qk  = self.query(x) / math.sqrt(x.size(-1))
        kq  = self.key(x).transpose(-2, -1) / math.sqrt(x.size(-1))
        attn_weight  = torch.softmax(qk @ kq, dim=-1)  # Apply softmax to the result
        attn_weight  = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        v   = self.value(x)  # Compute the dot product of the dropout output and the value
        return (attn_weight @ v).transpose(-2, -1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
