
class AttentionModel(torch.nn.Module):
    def __init__(self, inv_scale=4):
        super().__init__()
        self.inv_scale  = torch.nn.Parameter(torch.tensor([inv_scale]))
        self.key = torch.nn.Parameter(torch.randn(1024, 36)) # 36 because we are not interested in the dimensionality of the key vectors in this example.
        self.query = torch.nn.Parameter(torch.randn(180, 36))

    def forward(self):
        scaled_dot_product  = torch.matmul(self.query, self.key.transpose(-2, -1)) / self.inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(self.value)

# Initializing the model
m  = AttentionModel()

 # Inputs to the model
query = torch.randn(32, 36) # query is of dimension (batch size x number of elements per batch)
key = torch.randn(1024, 36) # key and value are of dimension [batch_size x number of elements per batch x embedding size] in this example. We are not interested in the embedding size for this example.
__output__  = m()

