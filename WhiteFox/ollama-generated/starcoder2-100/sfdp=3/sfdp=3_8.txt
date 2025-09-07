
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        v2  = v1 * scale_factor
        v3  = v2.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=dropout_p) 
        __output__  = v4.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return __output__


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(1, 200, 768)
key    = torch.randn(3, 200, 768)
value  = torch.randn(3, 200, 512)
scale_factor  = float(0.9999999403953552) # A scaling factor is randomly generated as input to the model for each new test example
dropout_p     = float(0.8756920719146729)  # A dropout probability value is randomly generated as input to the model for each new test example

