
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_1 = torch.nn.Linear(768, 32)
        self.attention_2 = torch.nn.Linear(32, 768)
        self.projection = torch.nn.Linear(768, 768)
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / (torch.sqrt(torch.tensor(key.shape[-1]))) # Scale the dot product by sqrt(dim).
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)  # Multiplication with softmax, then multiplication of this with value
        projection = self.projection(torch.tanh(self.attention_2(attention_weights.matmul(self.attention_1(output))))))
        return projection


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(1, 768) # The query tensor of shape (batch_size, num_attention_heads * head_dim)
key  = torch.randn(1, 768) # The key tensor of shape (batch_size, num_attention_heads * head_dim)
value  = torch.randn(1, 768) # The value tensor of shape (batch_size, num_attention_heads * head_dim)
