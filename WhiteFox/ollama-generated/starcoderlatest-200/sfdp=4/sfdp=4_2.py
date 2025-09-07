
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = None
 
    def forward(self, q1, k1, v1):
        attn_weight = torch.softmax((q1 @ k1.transpose(-2, -1) / math.sqrt(q1.size(-1))), dim=-1) # Compute the dot product of the query and key, and scale it

        output = self.attn_mask * v1  + attn_weight * torch.cat((v1, v1, v1), dim=-2) # Apply softmax to the result
        return output


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(1, 3, 64, 64)
k1 = torch.randn(1, 8, 64, 64)
v1 = torch.randn(1, 8, 64, 64)
m.__output__(q1, k1, v1)

