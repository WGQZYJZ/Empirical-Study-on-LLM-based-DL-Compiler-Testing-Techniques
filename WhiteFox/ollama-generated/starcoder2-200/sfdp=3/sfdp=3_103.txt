
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Parameter(data=torch.rand([2048, 768]), requires_grad_=True) # Shape [2048, 768]
        self.key  = torch.nn.Parameter(data=torch.rand([512, 399790]), requires_grad_=True) # Shape [512, 399790]

    def forward(self, x):
        scale_factor  = torch.nn.Parameter(data=torch.rand([]), requires_grad_=True) # Scale the dot product by a factor.
        dropout_p  = torch.nn.Parameter(data=torch.rand([]), requires_grad_=True) # Apply dropout to the softmax output
        value  = torch.nn.Parameter(data=torch.rand([512, 399790]), requires_grad_=True) # Shape [512, 399790]

        qk  = torch.matmul(self.query, self.key.transpose(-2, -1))
        scaled_qk  = qk.mul(scale_factor) 
        softmax_qk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  
        output  = dropout_qk.matmul(value)
        return output

# Initializing the model
m  = Model()


# Inputs to the model