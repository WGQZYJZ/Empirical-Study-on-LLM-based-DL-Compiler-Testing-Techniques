
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk):
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()
# Inputs to the model
qk = torch.randn(32, 64, 16)
