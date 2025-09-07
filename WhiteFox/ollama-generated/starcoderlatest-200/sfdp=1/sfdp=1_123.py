
class MultiheadAttention(torch.nn.Module):
    def __init__(self, input_dim: int, num_heads: int = 8, dropout_p: float = 0.1, scale_factor: float = 4):
        super().__init__()
        self.input_dim = input_dim
        self.num_heads = num_heads
        self.scale_factor = scale_factor
 
        self.query = torch.nn.Linear(input_dim, input_dim, bias=False) 
        self.key = torch.nn.Linear(input_dim, input_dim, bias=False) 
        self.value = torch.nn.Linear(input_dim, input_dim, bias=False) 
        self.out = torch.nn.Linear(input_dim, input_dim)
 
        self.dropout = torch.nn.Dropout2d(p=dropout_p)
 
    def forward(self, x):
        qk = self.query(x).chunk(2, dim=-1)  # Split the query and key tensor in two parts
        query, key = qk[0], qk[1]
 
        scaled_qk = torch.matmul(query, key.transpose(-2, -1)) / self.scale_factor  # Compute the dot product of the query and key tensors and then scale by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)  # Apply dropout to the softmax output
 
        return self.out(torch.matmul(dropout_qk, self.value(x)))
 
class Model(torch.nn.Module):
    def __init__(self, input_dim: int = 128, num_heads: int = 4, num_layers: int = 2, dropout_p: float = 0.1, scale_factor: float = 4):
        super().__init__()
 
        self.input_dim = input_dim
        self.num_heads = num_heads
        self.scale_factor = scale_factor
 
        self.attentions = torch.nn.ModuleList([
            MultiheadAttention(input_dim, num_heads=num_heads, dropout_p=dropout_p, scale_factor=scale_factor)
            for _ in range(num_layers)
        ])
 
        self.out = torch.nn.Linear(input_dim, input_dim)
 
    def forward(self, x):
        attention = sum([att(x) for att in self.attentions])  # Combine the output of multiple attention layers to compute the representation vector from the sequence
        
        return self.out(attention)
 
 