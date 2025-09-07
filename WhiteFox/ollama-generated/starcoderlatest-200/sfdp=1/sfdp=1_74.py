
class Attention(torch.nn.Module):
    def __init__(self, query_dim, key_dim, scale_factor, num_heads=1):
        super().__init__()
        self.query_layer = torch.nn.Linear(query_dim, 4 * scale_factor * num_heads)
        self.key_layer = torch.nn.Linear(key_dim, 4 * scale_factor * num_heads)
        self.scale_factor = scale_factor
        self.num_heads = num_heads
 
    def forward(self, query, key):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(self.scale_factor) # Scale the dot product by the scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1) # Apply dropout to the softmax output
        output = dropout_qk.matmul(self.scale_factor * value) # Compute the dot product of the dropout output and the value tensor
        return output
 
class Transformer(torch.nn.Module):
    def __init__(self, query_dim, key_dim, scale_factor):
        super().__init__()
        self.attention = Attention(query_dim, key_dim, scale_factor)
 
    def forward(self, query, key):
        output  = self.attention(query, key) # Apply the attention mechanism on the query and the key tensor
        return output
 
class Model(torch.nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.transformer1 = Transformer(32, 32, 4)
        self.fc = torch.nn.Linear(4 * 8, num_classes)
 
    def forward(self, x):
        v1 = self.transformer1(query=x[:, :, :32], key=x[:, :, 64:]) # Apply the transformer on the query and the key tensor
        v2 = torch.nn.functional.avg_pool2d(v1, (2, 2)) # Compute the average pooling of the output
        v3 = self.fc(v2)
        return v3
 
model = Model()
input = torch.randn(10, 3, 64, 64)
