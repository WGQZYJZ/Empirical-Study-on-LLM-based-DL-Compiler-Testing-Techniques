
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 1e4
        self.dropout_p = 0.5
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = v1 / math.sqrt(self.scale) # Scale the dot product by a scaling factor
        v3  = self.dropout_p
        v4  = torch.nn.functional.dropout(scaled_qk, p=v3) # Apply dropout to the softmax output of the scaled dot product
        v5  = value
        v6  = torch.matmul(v4, v5) # Compute the dot product of the dropout output and a value tensor
        return v6
 
# Initialize the model
model = Model()

# Inputs to the model
q1_data = torch.randn(20, 32, 768)
k1_data = torch.randn(20, 32, 768)
v1_data = torch.randn(20, 32, 512)
q1 = torch.tensor([q1_data]) # Define a dummy query tensor with batch size of 1 and the shape (batchsize, sequence length, embedding dimension)
k1 = torch.tensor([k1_data]) # Define a dummy key tensor with batch size of 1 and the shape (batchsize, sequence length, embedding dimension)
v1 = torch.tensor([v1_data]) # Define a dummy value tensor with batch size of 1 and the shape (batchsize, sequence length, embedding dimension)
 
# Initializing the model
m = Model()

# Inputs to the model
x1 = q1
x2 = k1
x3 = v1

