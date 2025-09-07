
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = torch.ones([8, 2, 1, 64])

    def forward(self, x, y):
        attn_weight = torch.matmul(x, y) / math.sqrt(x.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_weight = attn_weight + self.attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(attn_weight) # Apply softmax to the result

        output = attn_weight @ y  # Compute the dot product of the attention weights and the value

        return output


# Initializing the model
m = Model()

# Inputs to the model
x1, y1 = torch.randn(8, 2, 64), torch.randn(8, 8, 64)
