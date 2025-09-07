
class Model(torch.nn.Module):
    def __init__(self, d_k, nhead=8):
        super().__init__()
        self.scale = 1 / math.sqrt(d_k)
        self.nhead = nhead
        self.qkv = torch.nn.Linear(d_model, (d_k * nhead))
 
    def forward(self, q, k, v):
        batch_size = q.shape[0]  # Batch size
        head_size = self.nhead  # Number of heads in the Transformer
        query_layer = torch.nn.Linear(batch_size, d_k).weight
        key_layer = torch.nn.Linear(batch_size, d_k).weight
        value_layer = torch.nn.Linear(batch_size, d_v).weight
        layer1 = self.qkv(query_layer)  # Calculate the dot product of the query and the key matrix
        layer2 = layer1 * self.scale  # Scale the dot product by a constant `self.scale`
        layer3 = torch.nn.Softmax(dim=-1)(layer2)  # Apply softmax to the scaled dot product matrix
        layer4 = torch.matmul(layer3, key_layer)  # Compute the dot product of the dropout output and the value vector
        return layer4


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1024, d_k)  # Shape `[batch_size, seq_length, d_k]`
key = torch.randn(1024, d_k)  # Shape `[batch_size, seq_length, d_k]`
value = torch.randn(1024, d_v)  # Shape `[batch_size, seq_length, d_v]`
