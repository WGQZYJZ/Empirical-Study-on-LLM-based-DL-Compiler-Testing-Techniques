
class Model(torch.nn.Module):
    def __init__(self, d_k=64, nhead=8, dim_feedforward=2048, dropout_p=0.1):
        super().__init__()
        self.query = torch.nn.Linear(d_k, d_k)  # First linear layer
        self.key = torch.nn.Linear(d_k, d_k)  # Second linear layer
        self.value = torch.nn.Linear(d_k, dim_feedforward)  # Third linear layer
        self.scale = 1 / math.sqrt(dim_feedforward)
        self.dropout = nn.Dropout(p=dropout_p)
 
    def forward(self, x, attention_mask):
        # Calculate the key, query, and value tensors using dot product of matrix x and matrix y
        k = self.query(x).transpose(-1, -2)  # Get a view of (batch, seq_length, d_k) from the tensor
        v = self.key(x).transpose(-1, -2)  # Get a view of (batch, seq_length, d_k) from the tensor
        scaled_attention = k.matmul(v).div(self.scale)  # Calculate the dot product between the key and value tensors
        dropout_attention = self.dropout(F.softmax(scaled_attention, dim=-1))  # Apply dropout to calculate attention weights
        output = dropout_attention.matmul(self.value)  # Get a view of (batch, seq_length, dim_feedforward) from the tensor
        return output


# Initializing the model
m = Model()


