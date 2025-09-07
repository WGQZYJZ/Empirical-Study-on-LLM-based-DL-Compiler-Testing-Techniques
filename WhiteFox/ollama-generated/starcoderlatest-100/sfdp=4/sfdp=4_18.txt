
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, q1, k1, v1):
        (output_1, attn_weight_1) = self.attn(q1, k1, v1)
        return output_1, attn_weight_1


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(256, 3, 16, 16)
k1 = torch.randn(256, 8, 16, 16)
v1 = torch.randn(256, 8, 4, 4)
__output_1, __output_2 = m(q1, k1, v1)


# Checking the validity of the output from the model
assert (__output == __output_1).all(), 'the two outputs are different'
assert (__output == __output_2).all(), 'the two outputs are different'
