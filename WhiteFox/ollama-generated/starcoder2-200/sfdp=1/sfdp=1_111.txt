
class Attention(torch.nn.Module):
    def __init__(self, num_heads=8, inv_scale_factor=1024., dropout_p=.3):
        super().__init__()
 
        self.inv_scale_factor  = torch.tensor([inv_scale_factor], dtype=torch.float)
 
        self.query = torch.nn.Linear(768, 768 * num_heads) # Linear transformation with a number of output channels equal to the number of heads multiplied by the input channel dimensionality
        self.key = torch.nn.Linear(768, 768 * num_heads)
 
        self.value = torch.nn.Linear(768, 768 * num_heads)
 
        self.dropout = torch.nn.Dropout(p=dropout_p)
 
    def forward(self, x):
        q = self.query(x).div(torch.sqrt(torch.tensor([1024.], dtype=torch.float))) # Apply a scaling to the query vector and then apply linear transformation 
        k = self.key(x) # Compute the dot product of the query with key tensors using PyTorch APIs
        v = self.value(x)
 
        scaled_qk  = torch.matmul(q, k.transpose(-2, -1)) * 50
        scaled_qk  = scaled_qk / inv_scale_factor
        scaled_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(scaled_qk, p=0.3)
 
        output  = dropout_qk.matmul(v) # Compute the dot product of the dropout output and a value tensor using PyTorch APIs
        return output

# Initializing the model
m1 = Attention()
 
# Inputs to the model
x2 = torch.randn(4, 50, 768).to("cuda:0")

# Computing the model output with the initial model weights