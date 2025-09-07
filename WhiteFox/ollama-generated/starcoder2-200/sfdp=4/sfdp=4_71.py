
class Transformer(torch.nn.Module):
    def __init__(self, num_hidden: int = 64, num_layers: int = 12, attn_heads: int = 8) -> None:
        super().__init__()
 
        self.input_linear = torch.nn.Linear(784, num_hidden) # Apply pointwise convolution with kernel size 3 to the input tensor
        self.dropout = torch.nn.Dropout(0.5) # Add a dropout layer to randomly deactivate half of the elements in the tensor
        self.attn = ScaledDotProductAttention() # Initialize a scaled dot-product attention mechanism, which is used to compute the attention weights and then perform dot product operation
        
        self.output_linear = torch.nn.Linear(num_hidden, 32) # Apply pointwise convolution with kernel size 10 to the output tensor
        self.act = torch.nn.Tanh() # Apply hyperbolic tangent activation function to the output tensor
    
    def forward(self, x):
        query  = self.input_linear(x)  # Compute the dot product of the scaled dot-product attention weights and the value
        attn_mask = self.attn(query, key=query)  # Compute the dot product of the query and key tensors, then compute the relative position embedding using that result, then apply masking to it
        query = self.dropout(query + attn_mask)  
        
        v1  = self.output_linear(query) 
        return self.act(v1)


# Initializing the model
t  = Transformer()
__output__  = t(torch.randn(32, 64)) # Apply dropout to randomly deactivate half of the elements in the tensor

