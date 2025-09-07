
class MultiHeadAttentionLayer(torch.nn.Module):
    def __init__(self, dim_k: int = 64, num_heads: int = 8) -> None:
        super().__init__()
        self._num_heads = num_heads
 
        # Initialize the scale variable (for scaling the dot product)
        self.scale = torch.nn.Parameter(torch.tensor([math.sqrt(dim_k)]))
 
    def forward(self, query, key, value):
        # Get the batch size and number of features
        bs  = query.size()[0]
 
        # Scale the dot product of query and key (for normalization) by self._scale
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / \
            self.scale
 
        # Compute the attention weights based on scaled dot product
        attn_weights  = F.softmax(scaled_dot_product, dim=-1)
 
        # Apply dropout to attention weights
        attn_weights = F.dropout(attn_weights, p=0.5, training=self.training)
 
        # Compute the output by doing a weighted sum of the value
        attn_output  = torch.matmul(attn_weights, value)
 
        return attn_output

# Initializing the model with number of features and number of heads as inputs to the class constructor
m  = MultiHeadAttentionLayer(dim_k=64, num_heads=8)
 
# Inputs to the model
query  = torch.randn([320, 128]) # Query input tensor with shape [batch size x number of features]
key    = torch.randn([320, 128]) # Key input tensor with shape [batch size x number of features]
value  = torch.randn([320, 64*8]) # Value input tensor with shape [batch size x number of features * number of heads]
 
__output__  = m(query, key, value)

