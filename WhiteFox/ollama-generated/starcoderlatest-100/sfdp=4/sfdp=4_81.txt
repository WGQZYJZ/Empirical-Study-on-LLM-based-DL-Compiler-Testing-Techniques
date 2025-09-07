
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key_layer = torch.nn.Linear(768, 1024) # Linear layer for the key of the transformer
        self.value_layer = torch.nn.Linear(768, 1024) # Linear layer for the value of the transformer
 
    def forward(self, x):
        query = x
        query = query.permute([0, 3, 1, 2]) 
        key = self.key_layer(x)
        value = self.value_layer(x)
        attn_weight = torch.softmax(query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)), dim=-1) # Compute the dot product of the query and key, and scale it
        output = attn_weight @ value # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2048, 768) # (batch size, embedding dimension)
