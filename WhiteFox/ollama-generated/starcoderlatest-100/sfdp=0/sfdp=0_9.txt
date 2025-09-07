
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim=128, dropout=0.1):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=dropout)
        self.dim = dim
 
    def forward(self, query, key, value):
        n_batches  = query.size()[0]
        
        # Compute the scaled dot product attention matrix using a batch-oriented version of the attention calculation to make it scalable across different batch sizes and sequence lengths
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(self.dim)

        # Apply dropout before softmax
        attn_weights = self.dropout(scaled_dot_product.softmax(dim=-1))
        output = (attn_weights).matmul(value)

        return output


class Model(torch.nn.Module):
    def __init__(self, dim=128, dropout=0.1):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 1, stride=1, padding=1)
        self.fc = torch.nn.Linear(1024, dim)

        self.attention = ScaledDotProductAttention(dim=dim, dropout=dropout)

    def forward(self, x1):
        v1 = F.relu(self.conv1(x1))
        v2 = v1.view(-1, 1024) # Flatten the input tensor
        v3 = self.fc(v2)
        v4 = self.attention(v1, v2, v3)

        return v4

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
