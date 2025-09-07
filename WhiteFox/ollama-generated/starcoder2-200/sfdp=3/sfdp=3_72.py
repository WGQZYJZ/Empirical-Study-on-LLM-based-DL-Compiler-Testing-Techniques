
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=3, num_heads=2)
 
    def forward(self, query1, key1, value1, query2, key2, value2):
        o1  = self.attn(query1, key1, value1).sum() / len(key1) # Divide the output by number of keys in the batch
        o2  = self.attn(query2, key2, value2).sum() / len(key2) 
        return torch.cat([o1, o2], dim=0)


# Initializing the model
m = Model()
 
# Input tensors for the first query tensor of the model
query_tensor_one  = torch.randn((3, 5)) # Input tensor of size [batch x seq] - where batch is number of keys in the batch and seq is the length of each sequence per batch element.
key_tensor_one  = torch.randn(len(query_tensor_one), 4) # Key tensor of size [batch x seq] - where batch is number of keys in the batch and seq is the length of each sequence per batch element.
value_tensor_one  = torch.randn(len(key_tensor_one), 32, 8)
 
# Input tensors for the second query tensor of the model
query_tensor_two  = torch.randn((10, 5)) # Input tensor of size [batch x seq] - where batch is number of keys in the batch and seq is the length of each sequence per batch element.
key_tensor_two  = torch.randn(len(query_tensor_two), 4) # Key tensor of size [batch x seq] - where batch is number of keys in the batch and seq is the length of each sequence per batch element.
value_tensor_two  = torch.randn(len(key_tensor_one), 32, 8)
 
# Forward pass with both sets of input tensors
__output__  = m(query_tensor_one, key_tensor_one, value_tensor_one, query_tensor_two, key_tensor_two, value_tensor_two)

