
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 1

    def forward(self, x1): 
        scale = torch.full((3,), fill_value=self.scale)
        scaled_dot_product = torch.matmul(x1, x2.transpose(-2, -1)) / (torch.sqrt(torch.sum(scale)))
        attention_weights = scaled_dot_product.softmax(dim=-1) # Softmax
        output = attention_weights.matmul(x3)  # Compute a weighted sum of the values
        return output


# Initializing the model
m  = Model() 

# Inputs to the model
__inputs__  = torch.randn(8, 64)
__output__  = m(__inputs__)