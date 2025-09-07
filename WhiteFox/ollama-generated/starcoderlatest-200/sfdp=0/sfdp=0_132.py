
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, dim_model: int = 768):
        super().__init__()
        self.dim_model = dim_model
        self.num_heads = 2

        # Compute the dimension of each head to be used in multi-head attention
        d_h = self.dim_model // self.num_heads
        
        # Create two linear layers, one for each half of the heads (or channels) and one after the scaled dot product with a softmax on top of that 
        self.linear_qkv = torch.nn.Sequential(
            torch.nn.Linear(dim_model, d_h * 3, bias=False),
            torch.nn.GELU(),
            torch.nn.Linear(d_h * 3, dim_model, bias=False)
        )

        # The output of the two layers is then concatenated and a linear layer with a single neuron acts as the context vector for each head (or channel), so the dimension of the final vector has changed from d_model to num_heads * d_h
        self.linear_out = torch.nn.Sequential(
            torch.nn.Linear(dim_model, dim_model, bias=False),
            torch.nn.GELU(),
            torch.nn.Linear(dim_model, self.num_heads * d_h)
        )
    
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        # Compute the two linear transformations to convert the query and key to head dimensions before passing them into a linear layer
        qkv = self.linear_qkv(torch.cat((query, key, value), dim=-1))
        
        # The three linear layers are then applied with some additional computation in between
        h = torch.matmul(qkv[:, 0:d_model], attention_weights) + torch.matmul(qkv[:, d_h:2*d_model], attention_weights ** 2) + torch.matmul(qkv[:, 2*d_h:], attention_weights ** 3)
        
        # Return the output of the linear layers
        return self.linear_out(h).view(*query.shape, -1)


# Creating the model using the MultiHeadAttention module defined above
m = torch.nn.MultiHeadAttention(dim_model=768)


# Inputs to the model
query  = torch.randn(1, 32, 768)
key    = torch.randn(1, 64, 768)
value  = torch.randn(1, 64, 768)
