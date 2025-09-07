
class Attention(torch.nn.Module):
    def __init__(self, query_dim, key_dim, scale=None):
        super().__init__()
        self.query = torch.nn.Linear(query_dim, key_dim)  # Use Linear to reduce the dimensionality of the query
        self.key   = torch.nn.Linear(key_dim, key_dim)    # Use Linear to reduce the dimensionality of the key
        self.scale = scale if scale is not None else query_dim**-0.5
 
    def forward(self, q, k):
        v1 = self.query(q).unsqueeze(-2)  # Apply linear transformation (to be compatible with attention head) to the query tensor
        v2 = self.key(k)                          # Apply linear transformation (to be compatible with attention head) to the key tensor
        return torch.matmul(v1, v2.transpose(-2, -1)) * self.scale
 
class Model(torch.nn.Module):
    def __init__(self, n_classes=10):
        super().__init__()
 
        # Initialize a fully-connected layer with an input dimension of 16 and output dimension equal to the number of classes.
        self.fc = torch.nn.Linear(128, n_classes)
 
    def forward(self, x):
        return self.fc(x)
 
def main():
    # Create a model instance
    m = Model()
 
    # Get an example batch from the training data
    x = torch.randn(64, 3, 32, 32)
    y = torch.randint(0, 10, (64,))
 
    print('Example:')
    print('Input: {}'.format(x))
    print('Target: {}'.format(y))

    # Generate a valid PyTorch model example with public PyTorch APIs meets the specified requirements
    q = torch.randn((32, 8), dtype=torch.float) 
    k = torch.randn((32, 16), dtype=torch.float)
    v = torch.randn((16, 8), dtype=torch.float)
    scaled_qk = torch.matmul(q, k.transpose(-2, -1)) # (32, 8, 16) @ (16, 8, 16)^T => (32, 8, 16)
    softmax_qk = scaled_qk / math.sqrt(scaled_qk.shape[-1]) # (32, 8, 16) / sqrt((32, 8, 16))^T => (32, 8, 16)
    dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5) # Apply dropout to the softmax output 
    attention_output = torch.matmul(q, k.transpose(-2, -1)) * math.sqrt(scaled_qk.shape[-1]) # (32, 8, 16) @ (16, 8, 16)^T => (32, 8, 16)
    attention_output = torch.softmax(attention_output / math.sqrt(scaled_qk.shape[-1]), dim=-1) # Apply softmax to the scaled dot product of the query and key tensors
    attention_output = torch.nn.functional.dropout(attention_output, p=0.5)  # Apply dropout to the softmax output
    final_output = torch.matmul(attention_output, v) # (32, 8, 16) @ (16, 8, 8)^T => (32, 8, 8)
 
    print('Generated:')
    print('Query: {}'.format(q))
    print('Key: {}'.format(k))
    print('Value: {}'.format(v))
    print('Attention output shape: {}'.format(attention_output.shape))
    print('Output from attention layer: {}'.format(final_output))
 
    # Forward pass and check that the generated PyTorch model outputs match with the reference Python implementation result
    loss = nn.CrossEntropyLoss()(final_output, y)
    print('Loss: {}'.format(loss))
 
