
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1)) # Compute the dot product of query and key and scale it with the square root of the number of channels in the query tensor
        self.attn_weight = torch.softmax(self.qk + attn_mask, dim=-1)  # Apply softmax to the dot-product result and add an attention mask to it 
        self.output = torch.matmul(self.attn_weight, value)

    def forward(self):
        return self.output

# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(64, 1024) # Initialize a query tensor of shape (batch size, sequence length)
key    = torch.randn(32768, 512) # Initialize a key tensor with shape (sequence length, number of channels). It is typically very large to prevent the model from being exploded during training. It can be replaced by a one-hot mask if we know exactly which positions we want the model to attend to.
value = torch.randn(32768, 512) # Initialize a value tensor of shape (sequence length, number of channels). It is also very large and typically requires dynamic memory allocation during inference

