
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(8, 256) # Input: (batch_size, nhead, seq_len, head_dim) Output: (batch_size, nhead, head_dim, 2*query_length+7)
        self.conv = torch.nn.Conv2d(256, 8, 1, stride=1, padding=0) # Input: (batch_size, nhead, head_dim, 2*query_length+7) Output: (batch_size, nhead, head_dim, 32)
        self.linear2 = torch.nn.Linear(8*5, 16) # Input: (batch_size, nhead, head_dim, 32) Output: (batch_size, 16)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Shape of the input tensor is [1,8,32,1] and output tensor shape is [1,8,1,1].
        v2 = torch.nn.functional.softmax(v1, dim=1) # Softmax applied on output from conv layer
        v3 = torch.nn.functional.dropout(v2, p=0.5) # Apply dropout on the softmax output
        v4 = self.linear1(v3) # Shape of the input tensor is [1,8,1,1] and output tensor shape is [1,2,6,256].
        v5 = torch.nn.functional.softmax(v4, dim=-1) # Softmax applied on output from linear1 layer
        v6 = torch.nn.functional.dropout(v5, p=0.875) # Apply dropout on the softmax output
        v7 = self.linear2(v6).view(-1, 16) # Shape of the input tensor is [1,2,6,16] and output tensor shape is [1,4].
        return v7


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 6, 256)
