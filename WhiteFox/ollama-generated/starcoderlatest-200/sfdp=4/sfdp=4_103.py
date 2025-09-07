
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        qk = torch.einsum('bhnd,bdhn->bnhd', [x1, x2]).softmax(dim=-1)  # Compute the dot product of query and key, and scale it
        output = torch.einsum('bnhd,bdhn->bhnd', [qk, x2])  # Apply the softmax to the result and compute the weighted sum of values
        return output

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
