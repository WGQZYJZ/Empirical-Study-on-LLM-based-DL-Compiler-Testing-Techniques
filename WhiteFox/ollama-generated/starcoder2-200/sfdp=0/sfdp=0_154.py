
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.sqrt(torch.tensor([3]))
 
    def forward(self, input1, input2):
       dot = torch.matmul(input1, input2)  # Compute the scaled dot product of two matrices
       softmax_weights = F.softmax(dot / self.scale)  # Compute the attention weights as a softmax over the scaled dot product
       output = softmax_weights.mm(input2)  # Apply attention to compute a weighted sum over the value matrix (input2) using the softmax weights
       return output

# Initializing the model
m = Model()

# Inputs to the model
query1  = torch.randn(8, 512, 3074)  # Sampled query input tensor of size [batch_size x 8 x 512] with elements drawn from a standard normal distribution
key1    = torch.randn(64, 3074, 3074) # Sampled key matrix of size [batch_size x 64 x 3074] with elements drawn from a standard normal distribution
value1  = torch.randn(256, 3074, 8) # Sampled value tensor of size [batch_size x 256 x 8] with elements drawn from a standard normal distribution

__output__  = m(query1, key1), value1

