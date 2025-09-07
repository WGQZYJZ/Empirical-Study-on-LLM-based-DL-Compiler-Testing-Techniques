
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.softmax  = torch.nn.Softmax(dim=-1)
 
    def forward(self, query:torch.Tensor, key:torch.Tensor, value:torch.Tensor, scale_factor=1., dropout_p=0.) -> torch.Tensor:
        qk = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk  = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk = self.softmax(scaled_qk) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output  = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing model<|end_of_model|>
m = Model()
 
