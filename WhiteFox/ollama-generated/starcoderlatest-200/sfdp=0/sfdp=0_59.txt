
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scaled_dot_product = torch.nn.Linear(768, 32)
 
    def forward(self, x1, x2, key, value):
        scaled_dot_product = torch.matmul(x1, key.transpose(-2, -1)) / math.sqrt(x2.size()[-1]) # Compute attention weights with Scaled Dot-Product Attention mechanism in PyTorch
        attention_weights  = scaled_dot_product.softmax(dim=-1) # Apply the softmax function on the attention weights to obtain probability distributions over corresponding vector elements and perform matrix multiplication between these values and each row of `value`
        output  = attention_weights.matmul(value) # Use a weighted sum to compute an output representation given the key-value pair from the query-key correspondence table. The weighting operation is carried out elementwise.
        return output

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 768) # Query vector of shape [1, 3, 768]
x2 = torch.randn(1, 3, 768) # Key/Value tensor with shape [1, 3, 768]
query = torch.randn(512, 768) # Query vector of shape [1, 3, 768]
value = torch.randn(512, 768) # Key/Value tensor with shape [1, 3, 768]
