
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk  = torch.nn.Linear(8, 12)
 
    def forward(self, v1):
        qk = self.qk(v1) 
        qk_scaled  = qk * scale_factor  
        squeezed_qk  = torch.squeeze(qk_scaled)  # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(squeezed_qk, p=0.25)  # Apply dropout to the softmax output
        value1  = self.linear1(v1) 
        value2  = self.linear2(dropout_qk)  
        result  = torch.cat((value1, value2), dim=-1))  # Concatenate two vectors along the last dimension
        return result

# Initializing model
m  = Model()


Inputs to the model:
v1   = 0.9833556976318359  torch.Size([2, 12])  # A vector of shape (batch size x vector dimension)


Output from the model:<|output|>
