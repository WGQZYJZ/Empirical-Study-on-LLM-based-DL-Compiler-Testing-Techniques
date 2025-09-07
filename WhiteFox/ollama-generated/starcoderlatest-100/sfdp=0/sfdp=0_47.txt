
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(512, 8) # Apply linear transformation on feature dimension to generate query tensor
        self.key = torch.nn.Linear(512, 8) # Apply linear transformation on feature dimension to generate key tensor
        self.value = torch.nn.Linear(512, 8)
 
    def forward(self, x):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output

 # Initializing the model
m = Model()

 # Inputs to the model
x = torch.randn(1024, 512)
