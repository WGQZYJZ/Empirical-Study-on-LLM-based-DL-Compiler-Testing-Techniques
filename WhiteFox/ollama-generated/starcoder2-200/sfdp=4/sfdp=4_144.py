
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(256, 256)
        self.key   = torch.nn.Linear(256, 256)
        self.value = torch.nn.Linear(256, 256)
 
    def forward(self, query):
        v1 = query  # Query is the input tensor to the module
        v2 = self.query(v1)
        v3 = self.key(v1)
        v4 = v3.transpose(-2, -1)
        v5 = torch.norm(v2) / torch.sqrt(torch.Size([8])) # Compute the dot product of the query and key, and scale it
        v6 = v5 + attn_mask  # Add the attention mask to the scaled dot product
        v7 = torch.softmax(v6, dim=-1) 
        v8 = self.value(query)  # Compute the dot product of the attention weights and the value tensor
        return v8


# Initializing the model
a_model  = AttentionModel()


# Inputs to the model
a_model_input  = torch.randn(1, 256, 8)


