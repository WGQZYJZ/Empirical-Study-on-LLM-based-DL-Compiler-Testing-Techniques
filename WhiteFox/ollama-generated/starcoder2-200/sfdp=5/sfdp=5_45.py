
class MyModel(torch.nn.Module):
    def __init__(self, attn_head=4):
        super().__init__()
 
        # Inputs:
        # key: batch_size x key_length x input_dim
        self.query = torch.nn.Linear(input_dim, attn_head * query_length)
        self.key = torch.nn.Linear(input_dim, attn_head * key_length)
        self.value = torch.nn.Linear(input_dim, input_dim)
        # Output:
        # batch_size x value_length x output_dim
 
        # Softmax for the attention weights
        self.softmax = torch.nn.Softmax(dim=-1)
 
        # Dropout for regularization
        self.dropout = torch.nn.Dropout(0.3)
 
    def forward(self, key):
        qk  = self.query(key)
        k = self.key(key).transpose(-2, -1)
        v  = self.value(key)
 
        # Compute the dot product of the query and key (plus an attention mask), scale it with
        # the length of the key dimension, and then apply softmax to get the attention weights.
        qk  = qk @ k / math.sqrt(query_length) + attn_mask
        qk = self.softmax(qk)
 
        # Apply dropout to the attention weight.
        attn_weights  = self.dropout(attn_weight)
 
        output  = v * attn_weights.transpose(-2, -1).contiguous() 
        return output

model = MyModel()

# Initializing model parameters:
torch.nn.init.uniform_(model.query.weight) # Initialize the query layer weights with a uniform distribution in [0, 1]
torch.nn.init.uniform_(model.key.weight) # Initialize the key layer weights with a uniform distribution in [0, 1]

 # Input to the model:
input_data = torch.randn(batch_size=256, query_length=768, input_dim=392, key_length=392)
  