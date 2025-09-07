
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer = torch.nn.Linear(768, 512)
    
    def forward(self, x1):
        x = x1
        v = self.attn_layer(x).transpose(-1, -2) # Compute the attention weights of the input tensor `v` by using linear layer and transposing to obtain the shape `(batch_size, 512)`
        x = torch.softmax(v, dim=-1) # Apply softmax function over the attention weights
        x = x * self.attn_layer(x).transpose(-1, -2) # Compute the dropout output `v` with the attention weights by using linear layer and transposing to obtain the shape `(batch_size, 512)`
        v = torch.softmax(x, dim=-1) # Apply softmax function over the dropout output `v`. The value should have higher probability of appearing in the output than the query
        return torch.bmm(x, self.attn_layer(x).transpose(-1, -2)) # Compute the final output by using bilinear layer to obtain the shape `(batch_size, 512)`

# Initializing the model
m = Model()


