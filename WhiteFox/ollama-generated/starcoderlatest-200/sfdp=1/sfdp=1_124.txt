
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul1 = torch.nn.Linear(3, 16) # Linear layers for query, key and value
        self.matmul2 = torch.nn.Linear(3, 16) # Multiply the result of linear layer by a constant to apply the same transformation as in attention module 
        self.softmax = torch.nn.Softmax(dim=-1) # Apply softmax on the result of multiplication
        self.dropout = torch.nn.Dropout2d(p=0.5) # Apply dropout to the results of softmax
    def forward(self, x):
        q  = self.matmul1(x)
        k  = self.matmul1(x)
        v  = self.matmul2(x)
        scaled_qk  = q * k.transpose(-2,-1) / (v * torch.sqrt(scale_factor))
        softmax_qk  = scaled_qk.softmax(dim=-1) # Softmax on the results of dot product multiplication
        dropout_qk  = self.dropout(softmax_qk) # Dropout on the result of attention 
        output      = qk.matmul(v).transpose(-2, -1) # Dot product between dropout outputs and values 
        return output
 
