
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        qk = self.conv(x1).unsqueeze(-1) @ self.conv.weight.unsqueeze(-2) # Compute the dot product of the query and key, and scale it
        kd = torch.diag_embed(self.conv.weight.new_ones((1, 8))) # Get a diagonal embedding tensor with all ones on the diagonal
        kd[0][-1] = -kd[0][-1] # Make the diagonal of the embedding tensor negative
        qk *= math.sqrt(x1.size(-2)) # Scale the dot product of the query and key, and keep the square root of each term
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = (attn_weight @ x1).sum(dim=0) # Compute the dot product of the attention weights and the value

        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
