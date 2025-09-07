
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 256)
        self.key   = torch.nn.Linear(768, 256)
        self.value = torch.nn.Linear(768, 1024)
 
    def forward(self, x):
        query    = self.query (x).flatten(end_dim=2) # Shape (B, N, H * W), with N being the number of pixels in each feature map in x
        key      = self.key   (x).flatten(end_dim=2) # Shape (B, N, H * W), with N being the number of pixels in each feature map in x
        value    = self.value (x).flatten(end_dim=1) # Shape (B, N, HW)

        qk   = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it
        attn_weights = torch.softmax(qk, dim=-1)                           # Apply softmax to the result

        output = attn_weights @ value                                        # Compute the dot product of the dropout output and the value

        return output


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(5, 768)
