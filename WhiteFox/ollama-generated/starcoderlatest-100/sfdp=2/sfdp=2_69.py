
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(dim_per_head=512, num_heads=4)
 
    def forward(self, query, key, value):
        v1, s1 = self.attention(query, key, value, need_weights=False)  # MultiHeadAttention takes in a batch of queries and keys and returns outputs containing values, weights, and attention distribution for each head
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4096, 512, 256, 8)
x2 = torch.randn(4096, 512, 256, 8)
x3 = torch.randn(4096, 512, 256, 8)


# Outputs of the model (batch x head x length x size_per_head)
__output1__ = m(x1, x2, x3)

