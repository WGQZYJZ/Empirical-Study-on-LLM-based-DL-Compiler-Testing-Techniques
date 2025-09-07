
class Model(torch.nn.Module):
    def __init__(self, d_model=768):
        super().__init__()
        self.d_model = d_model
        self.qk = torch.nn.Linear(d_model * 2, d_model)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, dropout_p=0):
        v1 = self.qk(torch.cat([query, key], dim=-1)) # Compute the dot product of a query tensor and two copies of the key tensor concatenated on the last dimension
        v2  = v1 / math.sqrt(self.d_model)
        v3 = torch.nn.functional.softmax(v2, -1)
        v4 = torch.nn.functional.dropout(v3, p=dropout_p) # Apply dropout to the softmax output of the dot product
        v5  = value @ v4  # Compute the dot product of a value tensor and the dropout output of the dot product 
        return v5

# Initializing the model
m  = Model()
 
# Inputs to the model
query_tensor = torch.randn(2, 768)
key1_tensor = torch.randn(2, 32, 768) # A key tensor with 32 rows and a column size of 768 each.
value_tensor = torch.randn(2, 32, 50)
 
# Calculating the output from the model
