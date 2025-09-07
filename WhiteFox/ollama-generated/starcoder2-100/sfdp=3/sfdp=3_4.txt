
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.nn.Parameter(
            torch.empty(()), requires_grad=True)
        self.dropout  = torch.nn.Dropout(p=0.25)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):

        # Compute the dot product of the query and key tensors
        qk = torch.matmul(query, key.transpose(-2, -1))
        
        # Scale the dot product by a factor
        scaled_qk = qk.mul_(self.scale)

        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = self.dropout(softmax_qk)  # Apply dropout to the softmax output
 
        output = torch.matmul(dropout_qk, value) # Compute the dot product of the dropout output and the value tensor
        
        return output

m  = AttentionModel()

