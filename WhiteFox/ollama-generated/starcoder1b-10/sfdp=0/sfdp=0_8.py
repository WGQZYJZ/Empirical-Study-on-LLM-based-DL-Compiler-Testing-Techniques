
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        # Compute the dot product of `x1` and its own inverse square root to produce a scaling factor for softmax
        inv_scale = (torch.pow(x1.view(-1).pow(2), 0.5)).view(*x1.shape[:-1], 1)
        
        # Get the attention weights using the Scaled Dot-Product Attention mechanism
        scaled_dot_product = torch.matmul(x1, inv_scale)
        attention_weights = scaled_dot_product.softmax(dim=-1)

        # Perform a weighted sum to compute `output`
        output = attention_weights.matmul(x1)
        
        return output


# Initializing the model
m = Model()


