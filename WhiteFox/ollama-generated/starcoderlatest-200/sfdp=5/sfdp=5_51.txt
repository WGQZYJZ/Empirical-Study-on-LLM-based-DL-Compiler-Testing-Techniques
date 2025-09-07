
class Model2(torch.nn.Module):
    def __init__(self, input_dim=16):
        super().__init__()
        self.linear = torch.nn.Linear(input_dim, 32)
        self.softmax = torch.nn.Softmax(-1)
 
    def forward(self, qk, attn_mask):
        attn_weight = self.softmax(qk) + attn_mask
        output = torch.matmul(attn_weight, v)
        return output

# Initializing the model
m2 = Model2()


# Inputs to the model
x1 = torch.randn(1024, 32) # The first dimension is batch size and the second dimension is the number of keys in this example.
