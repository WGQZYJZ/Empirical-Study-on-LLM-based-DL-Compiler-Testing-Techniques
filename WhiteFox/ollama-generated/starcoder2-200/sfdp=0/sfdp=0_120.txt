
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, scale=None):
            # Scaled dot product attention with optional scaling
            scaled = torch.matmul(query, key.transpose(-2,-1)) / ((scale ** 0.5) if scale is not None else 1.)
            weights = scaled.softmax(dim=-1)
            output = weights.matmul(value)
 
            return output
 
# Initializing the model
m = Model()

